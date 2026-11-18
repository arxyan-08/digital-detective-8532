# Mission 3 — Understand the Operating System

## 1. Task / objective
Investigate my operating system environment, account identity, storage space, running processes, file paths, and file permissions using Terminal, and explain the core responsibilities of an operating system in my own words.

## 2. Work completed

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| --- | --- | --- |
| Operating system / system details (`sw_vers`, `uname -srm`) | Identifies the operating system name, version, kernel name, and processor architecture. | Running **macOS 27.2.1** on the **Darwin 27.2.0** kernel with **arm64** (Apple Silicon) architecture. |
| Current account identity (`whoami`) | Shows which user account is currently logged in and owns new files or Terminal commands. | Returned `[redacted]`, confirming commands run under my standard non-root user account. |
| Available and used storage (`df -h /`) | Displays total disk capacity, space currently used, and free space available in human-readable units. | Root volume total size `460Gi`, system volume `13Gi` used, and `345Gi` available. |
| System activity snapshot (`top -l 1 -n 5`) | Gives a live summary of total processes, CPU load, and physical RAM utilization. | Showed 825 total processes (3 running, 822 sleeping), ~5.5% user CPU / ~12.6% system CPU / ~82.4% idle, and 15G physical memory in active/cached use. |

---

### Task 3.2 — Understand processes
Using `ps -eo pid,comm` and `top -l 1 -n 5`, I viewed active user applications and background system services along with their process identifiers.

- **What is a process?** A process is an active instance of a program that is currently loaded in memory and running (or waiting to run) on the computer. A saved app on disk is just a file; once you launch it, the OS creates a process for it.
- **What does the PID column represent?** **PID** stands for **Process Identifier**—a unique positive integer assigned by the operating system to track and manage each running process (for example, `PID 1` on macOS is always `launchd`, the first system process started at boot).
- **Two examples of processes running on my computer:**
  1. `launchd` (`PID 1`) — A background macOS system process that starts and manages other system daemons and services.
  2. `zsh` (Terminal shell) and `com.apple.WebKit` (web browser rendering engine) — User-facing processes that run my shell commands and display web pages.

---

### Task 3.3 — Understand paths and permissions
- **Navigating between folders:** Starting in `/Users/[redacted]/digital-detective-8532` and running `cd mission-02-terminal/terminal-practice` changed `pwd` to `/Users/[redacted]/digital-detective-8532/mission-02-terminal/terminal-practice`.
- **Absolute path vs. relative path:**
  - An **absolute path** starts from the very top root directory `/` and specifies the exact location of a file regardless of which folder you are currently inside.
    - *Example from my repo:* `/Users/[redacted]/digital-detective-8532/mission-02-terminal/terminal-practice/notes.txt`
  - A **relative path** starts from your *current working directory* (without a leading `/`), so it is shorter and depends on where you currently are.
    - *Example from my repo (when inside `digital-detective-8532`):* `mission-02-terminal/terminal-practice/notes.txt`
- **Permission meanings:**

| Permission | Meaning | Example |
| --- | --- | --- |
| `r` — Read | Allows a file's contents to be viewed (or a folder's file list to be seen). | Opening `notes.txt` with `cat`. |
| `w` — Write | Allows a file to be modified or saved (or files to be added/deleted inside a folder). | Appending a line to `notes.txt`. |
| `x` — Execute | Allows a file to be run as a program; on a directory, allows entering/traversing it with `cd`. | Running a script or opening a subfolder. |

- **Owner permission check on my practice file:**
  Running `ls -l mission-02-terminal/terminal-practice/notes.txt` returned:
  `-rw-r--r--@ 1 [redacted] staff 103 ... notes.txt`
  - The first character `-` means it is a regular file (not a directory `d`).
  - The next three characters (`rw-`) are the **owner permissions**:
    - `r` -> Owner **can read** the file.
    - `w` -> Owner **can write/edit** the file.
    - `-` -> Owner **cannot execute** the file as a program (which makes sense because it is a plain text note, not a script).
  - No system permissions were modified.

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| --- | --- | --- |
| **Process management** | Starts, schedules, pauses, and terminates running programs so multiple apps can share the CPU smoothly without freezing the computer. | Switching rapidly between a web browser, VS Code, and Terminal while background services like `fseventsd` keep running. |
| **Memory management** | Allocates RAM to each running process, prevents programs from overwriting each other's memory, and frees RAM when apps close. | Giving RAM to open browser tabs and compressing or reclaiming memory when tabs are closed. |
| **Device management** | Communicates with connected hardware using drivers so applications can use devices without knowing low-level hardware details. | Handling input from the built-in keyboard/trackpad or sending audio to Bluetooth headphones. |
| **File management** | Organizes data into files and directories on storage drives, tracks where bytes live on disk, and enforces naming and hierarchy rules. | Creating folders like `mission-03-operating-system/` and saving `README.md` onto the SSD. |
| **User interface / shell** | Provides ways for humans to interact with the computer, either graphically (GUI) or through text commands (CLI). | Using macOS Finder windows (GUI) or typing commands inside Terminal running `zsh` (CLI). |
| **Security and permissions** | Controls user accounts, authentication, and read/write/execute rights so unauthorized users or apps cannot damage protected files. | Restricting system folders so a standard user cannot delete critical OS files without explicit authorization. |

## 3. Commands / tools used
- `sw_vers` and `uname -srm` — Checked macOS version, kernel version, and CPU architecture.
- `whoami` — Checked the active user account name.
- `df -h /` — Checked disk capacity, used storage, and available free space.
- `top -l 1 -n 5` — Captured a single non-interactive snapshot of CPU, memory, and process activity.
- `ps -eo pid,comm` — Listed running processes with their PIDs and command names.
- `pwd`, `cd`, and `ls -l` — Compared absolute/relative paths and inspected file permissions on `notes.txt`.

## 4. My understanding
The operating system sits between hardware and applications, acting like a traffic controller and caretaker for the entire computer. Seeing hundreds of background processes running even when I only have a couple of windows open showed how much invisible coordination macOS handles every second. Understanding absolute vs. relative paths makes Terminal navigation much clearer, and reading `rwx` permission strings explains how the OS protects files from accidental or unauthorized changes.

## 5. Difficulties faced
Running plain `top` updates continuously and takes over the Terminal screen until manually quit, and raw outputs from `whoami` and `ls -l` included my personal account username.

## 6. How I resolved them
Used `top -l 1 -n 5` (one-shot logging mode limited to 5 processes) to capture a clean snapshot cleanly, and redacted my username to `[redacted]` in both the evidence file and this README.

## 7. Evidence / files
- [mission-03-operating-system/README.md](README.md) — OS exploration table, process Q&A, paths and permissions breakdown, and OS responsibilities table.
- [evidence/mission-03-os-output.txt](../evidence/mission-03-os-output.txt) — Redacted Terminal outputs for `sw_vers`, `uname`, `df`, `top`, `ps`, and `ls -l`.

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Push status:** Committed on `main` (staged and committed separately from Mission 2; ready to push to GitHub).
