# Code Runner — Multi-Language Lab ⚡

Run **C**, **Python**, **SQL**, and **HTML** code from a single tool. Includes interactive guides for all four languages.

## 🔗 Links

| Link | URL |
|------|-----|
| **Live Site** | [`https://anomalyco.github.io/code-runner`](https://anomalyco.github.io/code-runner) |
| **Web Runner** | [`/runner.html`](https://anomalyco.github.io/code-runner/runner.html) |
| **C Guide** | [`/c_programming_guide.html`](https://anomalyco.github.io/code-runner/c_programming_guide.html) |
| **Python Guide** | [`/python/index.html`](https://anomalyco.github.io/code-runner/python/index.html) |
| **HTML/CSS Guide** | [`/task-1/index.html`](https://anomalyco.github.io/code-runner/task-1/index.html) |

## 🖥 CLI Usage

```bash
# Auto-detect language from code
python run.py --code "print('hello')"

# Run a file
python run.py my_program.c

# Force a specific language
python run.py --lang sql --code "SELECT 1;"

# Interactive mode
python run.py -i
```

## 🌐 Live Server

```bash
pip install flask
python server.py
# → http://localhost:5000
```

## 🔍 Language Detection

| Language | Extension | Code Signature |
|----------|-----------|---------------|
| C | `.c` | `#include`, `int main()` |
| Python | `.py` | `def`, `import`, `print(` |
| SQL | `.sql` | `SELECT`, `INSERT`, `CREATE` |
| HTML | `.html` | `<!DOCTYPE html>`, `<html>` |
