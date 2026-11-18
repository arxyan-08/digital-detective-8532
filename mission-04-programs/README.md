# Mission 4 — How Programs Run

## 1. Task / objective
Write a simple Python program, run it from Terminal, and understand the difference between how compilers and interpreters work.

## 2. Work completed

### Task 4.1 — Creating and running a Python program
I made a file called `hello.py` with just one line:
```python
print("Hello from Python")
```
Then ran it:
```
$ python3 hello.py
Hello from Python
```
That's it — no compile step, no build process. I saved the file and immediately ran it. Python just read my code and executed it on the spot.

### Task 4.2 — Compiler vs interpreter

| | Compiler | Interpreter |
| --- | --- | --- |
| **When does translation happen?** | Translates the *entire* program before running it | Translates and runs code on the fly, line by line (or via bytecode) |
| **What does it produce?** | A standalone executable file (like `.exe` or `a.out`) that runs without the compiler | Direct output on screen — no separate file to run later |
| **Example** | `gcc` for C/C++, `rustc` for Rust | `python3` for Python, Node.js for JavaScript |
| **Main advantage** | Programs run faster once compiled; catches errors across the whole program upfront | Way faster to test — just save and run, no waiting for a build step |

**How I'd explain this:** A compiler is like translating an entire book before anyone reads it — takes time upfront but the finished book is fast to read. An interpreter is like having a live translator at a conference — slower overall, but you hear each sentence immediately.

Python is technically a mix of both — CPython compiles your `.py` file into bytecode behind the scenes and then interprets that bytecode — but from my perspective as a user, it felt purely interpreted: I typed `python3 hello.py` and got instant results.

## 3. Commands / tools used
- `python3 hello.py` — ran the script using Python 3.13.15

## 4. My understanding
The key difference is *when* the translation from human-readable code to machine instructions happens. With a compiler, you wait for the whole program to be translated first. With an interpreter, you get results immediately but it's doing the translation work at runtime. For learning and experimenting (like this assignment), interpreted languages like Python are great because I can change one line and re-run instantly.

## 5. Difficulties faced
No major difficulties — this was one of the simpler missions.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [hello.py](hello.py) — The one-line Python program
- [mission-04-programs/README.md](README.md) — Comparison table and explanation

## 8. Commit details
- **Message:** `Compare compilers and interpreters`
- Committed on `main` and pushed to GitHub.
