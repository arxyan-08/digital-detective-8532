# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective
Practise core command-line (CLI) operations inside the repository, safely create and modify practice files, explore how command flags and pipes work, and inspect the macOS package manager (Homebrew) without installing or removing any software.

## 2. Work completed

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| --- | --- | --- |
| Current-directory display (`pwd`) | Prints the full path of the folder I am currently working inside. | Displayed `/Users/[redacted]/digital-detective-8532`. |
| Directory listing (`ls`) | Lists visible files and subfolders in the current directory. | Showed `README.md`, `evidence`, and all nine `mission-*` folders in columns. |
| Detailed listing (`ls -l`) | Shows permissions, link count, owner, group, file size, modified date, and name for each item. | Each file and folder appeared on its own line with permission strings like `-rw-r--r--` and `drwxr-xr-x`. |
| Change directory (`cd ..` / `cd <folder>`) | Moves into the parent folder (`..`) or into a specified subfolder. | Running `cd ..` moved one level up to `/Users/[redacted]`; running `cd digital-detective-8532` returned to the repository. |
| Create directory (`mkdir`) | Creates a new empty folder at the specified path. | Created `mission-02-terminal/terminal-practice` cleanly without errors. |
| Create empty file (`touch`) | Creates a new empty file (or updates the timestamp if it already exists). | Created `sample.txt` with a size of `0B`. |
| Copy file (`cp`) | Duplicates an existing file to a new filename or folder, keeping the original untouched. | Copied `notes.txt` to `notes_backup.txt`; both files existed with the same 103-byte content. |
| Move / rename file (`mv`) | Moves a file to another folder or renames it in place. | Renamed `notes_backup.txt` to `notes_archive.txt`; the old filename disappeared and the content remained intact. |
| Display file contents (`cat`) | Prints the full text content of a file directly into Terminal. | Printed both lines stored inside `notes.txt`. |

---

### Task 2.2 — Practise file changes safely
Inside `mission-02-terminal/terminal-practice/`, I created `notes.txt`, wrote a first line using `>`, appended a second line using `>>`, verified both lines with `cat notes.txt`, copied it to `notes_backup.txt`, and renamed the backup to `notes_archive.txt`.

**Answers to reflection questions:**
- **Difference between replacing a file's contents (`>`) and adding text to the end (`>>`):** Using a single `>` overwrites (erases) anything previously stored in the file and replaces it with the new output. Using double `>>` appends the new text to the end of the file while preserving all existing lines.
- **Difference between copying a file (`cp`) and moving a file (`mv`):** Copying creates a second independent copy so both the original and the copy exist afterward. Moving relocates or renames the original file itself, so only one copy exists at the new name or location.
- **What information does `pwd` provide?** `pwd` (Print Working Directory) shows the complete absolute path from the root directory `/` down to the exact folder Terminal is currently inside, preventing accidental edits in the wrong folder.
- **Why is a directory-listing operation (`ls`) useful?** Because Terminal does not show folder icons automatically like Finder does; `ls` lets you verify what files exist, check exact spelling/capitalization, and confirm that commands like `touch`, `cp`, or `mv` worked as expected.

---

### Task 2.3 — Understand flags and pipes
- **Comparing `ls` vs. `ls -lah`:**
  - Plain `ls` only printed the three filenames (`notes.txt`, `notes_archive.txt`, `sample.txt`).
  - Adding `-l` (long detailed format), `-a` (all files, including hidden entries starting with `.` like `.` and `..`), and `-h` (human-readable sizes like `103B` and `0B` instead of raw bytes) transformed the output into a detailed table with permissions, ownership, timestamps, and readable sizes.
- **Using a pipe (`ls -la | head -n 4`):**
  - The pipe symbol `|` connects the standard output of the command on the left directly into the standard input of the command on the right without creating a temporary file.
  - The left side (`ls -la`) generates the full detailed list of files in the directory.
  - The right side (`head -n 4`) filters that stream and prints only the first 4 lines (`total 16`, `.`, `..`, and `notes.txt`).

---

### Task 2.4 — Understand package managers
- **Homebrew inspection (read-only):**
  - `brew --version` confirmed Homebrew is installed: `Homebrew 7.0.9`.
  - `brew list --formula` showed 22 managed command-line packages (including tools such as `git`, `ffmpeg`, `ca-certificates`, and `cowsay`). No software was installed or uninstalled.
- **Why package managers are useful:** A package manager automates finding, downloading, installing, updating, and removing software from trusted repositories using simple commands. It also handles dependencies automatically—installing any helper libraries a program needs—so developers avoid hunting down installers manually or dealing with broken versions.

## 3. Commands / tools used
- `pwd` — Displayed the current working directory path.
- `ls`, `ls -l`, `ls -lah` — Listed files in simple, detailed, all-files, and human-readable formats.
- `cd` — Changed between the repository folder, parent folder, and practice subfolder.
- `mkdir` — Created the `terminal-practice` folder inside `mission-02-terminal`.
- `touch` — Created an empty practice text file (`sample.txt`).
- `echo`, `>`, `>>` — Wrote an initial line and appended a second line to `notes.txt`.
- `cat` — Printed the contents of `notes.txt` to confirm both lines were saved.
- `cp` and `mv` — Created a backup copy and renamed it safely.
- `|` and `head -n 4` — Piped a detailed listing into `head` to preview only the first few lines.
- `brew --version` and `brew list --formula` — Checked Homebrew version and listed managed packages without making changes.

## 4. My understanding
The Terminal gives direct, precise control over files and tools using short composable commands. Flags (`-l`, `-a`, `-h`) customize how a single command behaves without needing separate programs, and pipes (`|`) let small single-purpose commands work together like building blocks. Being careful with `>` versus `>>` and checking `pwd` before making changes prevents accidental overwrites or working in the wrong directory.

## 5. Difficulties faced
When copying raw `ls -lah` output for evidence, my local macOS username appeared in the owner column on every line.

## 6. How I resolved them
I checked the saved output before committing and replaced my computer username with `[redacted]` so the evidence remains accurate and privacy-safe.

## 7. Evidence / files
- [mission-02-terminal/README.md](README.md) — Command reference table, reflections, flags/pipes analysis, and Homebrew notes.
- [mission-02-terminal/terminal-practice/notes.txt](terminal-practice/notes.txt) — Two-line text file created with `>` and `>>`.
- [mission-02-terminal/terminal-practice/notes_archive.txt](terminal-practice/notes_archive.txt) — Renamed backup copy of `notes.txt`.
- [mission-02-terminal/terminal-practice/sample.txt](terminal-practice/sample.txt) — Empty file created with `touch`.
- [evidence/mission-02-terminal-output.txt](../evidence/mission-02-terminal-output.txt) — Privacy-safe Terminal outputs for Mission 2.

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Push status:** Committed on `main` (staged and committed separately from Mission 1; ready to push to GitHub).
