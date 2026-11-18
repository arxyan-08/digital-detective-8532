# Mission 3 — Understand the Operating System

## 1. Task / objective
Explore what operating system I'm running, check who's logged in, see how much storage I have, look at running processes, understand file paths and permissions, and explain what the OS actually does.

## 2. Work completed

### Task 3.1 — Exploring my OS

| What I checked | How | What I found |
| --- | --- | --- |
| OS version | `sw_vers` and `uname -srm` | macOS 27.2.1, Darwin kernel 27.2.0, arm64 (Apple Silicon) |
| Who's logged in | `whoami` | `[redacted]` — my standard user account |
| Storage | `df -h /` | 460 GB total drive, 345 GB still free |
| System activity | `top -l 1 -n 5` | 825 processes running, ~82% CPU idle, 15 GB RAM in use |

What surprised me here was the **825 processes** number. I only had a few windows open, but hundreds of things were running in the background — system daemons, kernel tasks, services I'd never heard of. macOS is doing a LOT behind the scenes.

### Task 3.2 — Understanding processes
I used `ps -eo pid,comm` to list running processes:

- **What is a process?** It's a program that's currently loaded into memory and running (or waiting to run). The app sitting on your disk is just a file — once you launch it, the OS creates a process for it.
- **What's a PID?** Process Identifier — a unique number the OS assigns to each running process so it can keep track of them. `PID 1` on macOS is always `launchd`, the first thing that starts at boot.
- **Two examples from my Mac:**
  1. `launchd` (PID 1) — the system's starter process that launches everything else
  2. `com.apple.WebKit` — the browser engine rendering web pages in the background

### Task 3.3 — Paths and permissions
**Absolute vs relative paths:**
- Absolute path starts from `/` (the root): `/Users/[redacted]/digital-detective-8532/mission-02-terminal/terminal-practice/notes.txt`
- Relative path starts from wherever you are right now: `mission-02-terminal/terminal-practice/notes.txt` (works if I'm already inside the repo folder)

Think of absolute paths as a full street address and relative paths as "turn left, second door on the right."

**File permissions:**
Running `ls -l` on `notes.txt` showed `-rw-r--r--`. Breaking that down:
- `-` = regular file (not a directory)
- `rw-` = owner can **read** and **write**, but not execute (makes sense — it's a text file, not a script)
- `r--` = group can only read
- `r--` = everyone else can only read

| Permission | What it means | Example |
| --- | --- | --- |
| `r` (Read) | You can view the file's contents | Opening a text file with `cat` |
| `w` (Write) | You can modify the file | Editing and saving changes |
| `x` (Execute) | You can run the file as a program | Running a shell script |

### Task 3.4 — OS responsibilities

| Responsibility | What it does (my explanation) | Example |
| --- | --- | --- |
| Process management | Juggles all running programs so they share the CPU fairly without freezing each other | Switching between browser, VS Code, and Terminal smoothly |
| Memory management | Gives each app its own chunk of RAM and cleans up when apps close | Freeing RAM when I close browser tabs |
| Device management | Talks to hardware through drivers so apps don't need to know low-level details | Making my trackpad work or sending audio to Bluetooth headphones |
| File management | Organizes everything into files and folders on disk | Saving `README.md` into the right mission folder on my SSD |
| User interface / shell | Gives us ways to interact — either clicking around (GUI) or typing commands (CLI) | Using Finder windows or typing in Terminal |
| Security and permissions | Controls who can access what, using accounts and `rwx` rules | Preventing a regular user from deleting core system files |

## 3. Commands / tools used
`sw_vers`, `uname -srm`, `whoami`, `df -h /`, `top -l 1 -n 5`, `ps -eo pid,comm`, `pwd`, `cd`, `ls -l`

## 4. My understanding
The OS is like an invisible manager running the show. I never realized how much coordination happens just to keep my laptop working — hundreds of processes being scheduled, memory being allocated and freed, permissions being enforced. The `rwx` permission system clicked for me when I saw that my `notes.txt` had `rw-` for the owner — of course a text file doesn't need execute permission, that's only for scripts and programs.

## 5. Difficulties faced
Running `top` without flags took over my whole Terminal screen and kept updating endlessly. Also, every command that showed user info included my actual Mac username.

## 6. How I resolved them
Used `top -l 1 -n 5` to get a single snapshot instead of a live view, and replaced my username with `[redacted]` in all evidence files.

## 7. Evidence / files
- [mission-03-operating-system/README.md](README.md) — All tables and explanations
- [evidence/mission-03-os-output.txt](../evidence/mission-03-os-output.txt) — Redacted Terminal outputs

## 8. Commit details
- **Message:** `Document operating system and file management`
- Committed on `main` and pushed to GitHub.
