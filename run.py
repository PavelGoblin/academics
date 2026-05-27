#!/usr/bin/env python3
"""
run.py — Multi-Language Runner
Detects & executes C, Python, SQL, and HTML code.

Usage:
  python run.py file.c          # Run C file
  python run.py file.py         # Run Python file
  python run.py file.sql        # Run SQL file
  python run.py file.html       # Open HTML in browser
  python run.py --code "..."    # Auto-detect from code string
  python run.py --interactive   # Interactive mode
"""

import sys
import os
import subprocess
import tempfile
import webbrowser
import sqlite3
import io
import re
import argparse
from pathlib import Path


def detect_language(code: str, filename: str = "") -> str:
    ext_map = {
        ".c": "c",
        ".py": "python",
        ".sql": "sql",
        ".html": "html",
        ".htm": "html",
    }
    ext = Path(filename).suffix.lower()
    if ext in ext_map:
        return ext_map[ext]

    lines = code.strip().splitlines()
    first_lines = "\n".join(lines[:10])

    if re.search(r'#include\s*[<"]', first_lines):
        return "c"
    if re.search(r'^import |^from |^def |^class |^print\s*\(|^if __name__', first_lines, re.MULTILINE):
        return "python"
    if re.search(r'^\s*(SELECT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER|WITH)\b', first_lines, re.IGNORECASE):
        return "sql"
    if re.search(r'<!DOCTYPE html|<html[\s>]', first_lines, re.IGNORECASE):
        return "html"

    return "unknown"


def run_c(code: str) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "program.c"
        exe = Path(tmp) / "program.exe"
        src.write_text(code, encoding="utf-8")

        compile_result = subprocess.run(
            ["gcc", str(src), "-o", str(exe), "-Wall", "-Wextra"],
            capture_output=True, text=True, timeout=30
        )
        if compile_result.returncode != 0:
            return f"[COMPILE ERROR]\n{compile_result.stderr.strip() or compile_result.stdout.strip()}"

        run_result = subprocess.run(
            [str(exe)], capture_output=True, text=True, timeout=30
        )
        output = run_result.stdout or run_result.stderr
        return output.strip() if output.strip() else "(no output)"


def run_python(code: str) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "script.py"
        src.write_text(code, encoding="utf-8")

        result = subprocess.run(
            [sys.executable, str(src)],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            return f"[ERROR]\n{(result.stderr or result.stdout).strip()}"
        return result.stdout.strip() or "(no output)"


def run_sql(code: str) -> str:
    out = io.StringIO()
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA enable_load_extension = 0")

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
    result = out.getvalue().strip()
    return result or "(no output)"


def run_html(code: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8") as f:
        f.write(code)
        f.flush()
        path = f.name
    webbrowser.open(f"file://{path}")
    return f"Opened in browser: file://{path}"


RUNNERS = {
    "c": run_c,
    "python": run_python,
    "sql": run_sql,
    "html": run_html,
}


def run_code(code: str, filename: str = "", lang: str = ""):
    if not lang:
        lang = detect_language(code, filename)
    if lang == "unknown":
        return f"[ERROR] Could not detect language. Supported: C, Python, SQL, HTML"

    runner = RUNNERS.get(lang)
    if not runner:
        return f"[ERROR] No runner for language: {lang}"

    print(f"[{lang.upper()}] Running...\n")
    result = runner(code)
    print(result)


def interactive_mode():
    print("=== Multi-Language Runner (C / Python / SQL / HTML) ===")
    print("Type your code. End with '---' on its own line to run.")
    print("Type 'exit' to quit.\n")
    while True:
        print(">>> ", end="", flush=True)
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                return
            if line.strip() == "---":
                break
            if line.strip().lower() == "exit":
                return
            lines.append(line)
        code = "\n".join(lines)
        if not code.strip():
            continue
        print()
        run_code(code)
        print("\n" + "=" * 50 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Multi-Language Runner")
    parser.add_argument("file", nargs="?", help="File to run")
    parser.add_argument("--code", help="Code string to run")
    parser.add_argument("--lang", help="Force language (c, python, sql, html)")
    parser.add_argument("-i", "--interactive", action="store_true", help="Interactive mode")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if args.code:
        run_code(args.code, lang=args.lang or "")
        return

    if args.file:
        path = Path(args.file)
        if not path.exists():
            print(f"[ERROR] File not found: {args.file}")
            sys.exit(1)
        code = path.read_text(encoding="utf-8")
        run_code(code, filename=args.file, lang=args.lang or "")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
