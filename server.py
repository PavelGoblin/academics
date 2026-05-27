#!/usr/bin/env python3
"""
server.py — Live Web Server for Multi-Language Runner
Run with: python server.py
"""

from flask import Flask, request, jsonify, send_from_directory
import subprocess
import tempfile
import sqlite3
import io
import re
import os
import sys
from pathlib import Path

app = Flask(__name__, static_folder=".")

def run_c(code):
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "program.c"
        exe = Path(tmp) / "program.exe"
        src.write_text(code, encoding="utf-8")
        comp = subprocess.run(["gcc", str(src), "-o", str(exe), "-Wall", "-Wextra"],
                              capture_output=True, text=True, timeout=30)
        if comp.returncode != 0:
            return {"output": comp.stderr.strip() or comp.stdout.strip(), "error": True}
        run = subprocess.run([str(exe)], capture_output=True, text=True, timeout=30)
        out = run.stdout.strip() or run.stderr.strip() or "(no output)"
        return {"output": out}

def run_python(code):
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "script.py"
        src.write_text(code, encoding="utf-8")
        r = subprocess.run([sys.executable, str(src)], capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            return {"output": (r.stderr or r.stdout).strip(), "error": True}
        return {"output": r.stdout.strip() or "(no output)"}

def run_sql(code):
    out = io.StringIO()
    conn = sqlite3.connect(":memory:")
    statements = re.split(r';\s*\n', code.strip())
    for stmt in statements:
        stmt = stmt.strip()
        if not stmt:
            continue
        try:
            cursor = conn.execute(stmt)
            if stmt.upper().lstrip().startswith(("SELECT", "WITH", "PRAGMA")):
                cols = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                if cols:
                    out.write(" | ".join(cols) + "\n")
                    out.write("-" * (sum(len(c) for c in cols) + 3 * len(cols)) + "\n")
                    for row in rows:
                        out.write(" | ".join(str(v) for v in row) + "\n")
                    out.write(f"({len(rows)} rows)\n")
            else:
                out.write(f"(rows affected: {cursor.rowcount})\n")
        except Exception as e:
            out.write(f"[SQL ERROR] {e}\n")
    conn.close()
    return {"output": out.getvalue().strip() or "(no output)"}

def run_html(code):
    tmp = tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8")
    tmp.write(code)
    tmp.close()
    return {"output": f"Saved to: {tmp.name}", "file": tmp.name}


@app.route("/api/run", methods=["POST"])
def api_run():
    data = request.get_json(force=True)
    code = data.get("code", "")
    lang = data.get("lang", "")

    if not lang:
        from run import detect_language
        lang = detect_language(code)

    runners = {"c": run_c, "python": run_python, "sql": run_sql, "html": run_html}
    runner = runners.get(lang)
    if not runner:
        return jsonify({"output": f"Unknown language: {lang}", "error": True})

    try:
        result = runner(code)
        result["language"] = lang
        return jsonify(result)
    except Exception as e:
        return jsonify({"output": str(e), "error": True})


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(".", path)


if __name__ == "__main__":
    print("Starting Code Runner Server at http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
