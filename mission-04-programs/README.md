# Mission 4 — How Programs Run

## 1. Task / objective
Create and run a one-line Python program (`hello.py`) from Terminal, and compare how compilers and interpreters translate and execute source code.

## 2. Work completed

### Task 4.1 — Create and run a Python program
Created [hello.py](hello.py) inside `mission-04-programs/`:
```python
print("Hello from Python")
```
Ran the script from Terminal inside `mission-04-programs/`:
```text
$ python3 hello.py
Hello from Python
```
The output `Hello from Python` appeared immediately with no separate compilation step.

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| --- | --- | --- |
| **When translation / execution happens** | Translates the entire source-code program *before* it is run; the generated file is executed separately afterward. | Reads, translates, and executes the program *at runtime* (instruction by instruction or via bytecode on the fly). |
| **Typical output** | A standalone executable or machine-code binary file (such as `a.out` or `.exe`) that can run without the compiler. | Direct program results on screen (no standalone native executable file is produced for the user to run alone). |
| **One example** | `gcc` / `clang` (used for C and C++), or `rustc` (Rust). | `python3` (CPython for Python), or Node.js / browser JavaScript engines (which combine interpretation with JIT compilation). |
| **One advantage** | Compiled programs usually run faster once built and catch many syntax or type errors across the whole program before execution. | Faster edit-and-test cycle—you can run code immediately after saving changes, making experimentation and debugging very convenient. |

**Explanation in my own words:**
As shown in the comparison table, the main difference between a compiler and an interpreter is **when** translation happens and **what** it produces. A compiler translates the whole source program up front into a separate executable file (like in C or C++), so once it builds successfully, the program runs very quickly on its own. An interpreter, on the other hand, executes code directly at runtime (like when I ran `python3 hello.py`), producing the result immediately without needing a separate build step. Many modern languages—including Python—actually blend both ideas internally (for example, CPython compiles source code to bytecode behind the scenes and then interprets that bytecode).

## 3. Commands / tools used
- `python3 hello.py` — Invoked the Python 3 interpreter (`Python 3.13.15`) to execute `hello.py` and display `"Hello from Python"`.
- **Text editor / Markdown:** Used to create `hello.py` and document the comparison table.
- `git add` & `git commit` — Staged and committed the Mission 4 files cleanly.

## 4. My understanding
Computers cannot directly understand human-readable languages like Python or C—they need instructions translated into forms the processor or virtual machine can execute. Running `hello.py` with `python3` showed how smooth an interpreted workflow is: I saved one line of code and saw its output immediately. Comparing compilers and interpreters clarified why systems software often uses compiled languages for speed, while scripting, learning, and rapid prototyping often favor interpreted languages like Python.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [mission-04-programs/hello.py](hello.py) — Working one-line Python program that prints `"Hello from Python"`.
- [mission-04-programs/README.md](README.md) — Program run verification and compiler vs. interpreter comparison.

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Push status:** Committed on `main` (staged and committed separately from Mission 3; ready to push to GitHub).
