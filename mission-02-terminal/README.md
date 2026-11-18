# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective
Learn to use the command line to navigate folders, create and manage files safely, understand what flags and pipes do, and check out the Homebrew package manager.

## 2. Work completed

### Task 2.1 — Basic Terminal operations
I went through each operation one by one inside my repo folder:

| Command | What it does | What I saw |
| --- | --- | --- |
| `pwd` | Prints the full path of where I currently am | `/Users/[redacted]/digital-detective-8532` |
| `ls` | Lists files and folders in the current directory | Showed `README.md`, `evidence`, and all 9 mission folders |
| `ls -l` | Lists with details — permissions, size, date | Each item got its own line with stuff like `-rw-r--r--` and file sizes |
| `cd ..` | Moves up one folder | Went from the repo folder to my home directory |
| `mkdir` | Creates a new folder | Made `terminal-practice` inside `mission-02-terminal` |
| `touch` | Creates an empty file | Created `sample.txt` with 0 bytes |
| `cp` | Copies a file (original stays) | Copied `notes.txt` → `notes_backup.txt`, both existed afterward |
| `mv` | Moves or renames a file | Renamed `notes_backup.txt` to `notes_archive.txt` — old name gone, content intact |
| `cat` | Prints file contents to Terminal | Showed both lines I'd written inside `notes.txt` |

### Task 2.2 — Safe file practice
Inside `terminal-practice/`, I did the following:
1. Created `notes.txt` and wrote a first line using `echo "..." > notes.txt`
2. Added a second line with `echo "..." >> notes.txt` (double arrow = append)
3. Ran `cat notes.txt` and confirmed both lines were there
4. Copied it to `notes_backup.txt` and renamed the copy to `notes_archive.txt`

**Key takeaways:**
- **`>` vs `>>`:** Single arrow *replaces* everything in the file. Double arrow *adds* to the end without touching what's already there. I nearly lost content testing this — glad I tried it on a practice file first.
- **`cp` vs `mv`:** Copying makes two independent files. Moving just changes the name or location — there's still only one file.
- **Why `pwd` matters:** Terminal doesn't show you a folder icon like Finder does. Without `pwd`, you could accidentally create files in the wrong place and not realize it.
- **Why `ls` is useful:** It's how you check what's actually in a folder. After running `touch` or `cp`, I'd immediately run `ls` to confirm it worked.

### Task 2.3 — Flags and pipes
- **`ls` vs `ls -lah`:** Plain `ls` just shows names. Adding `-l` gives a detailed table, `-a` includes hidden files (like `.` and `..`), and `-h` shows sizes in human-readable format (`103B` instead of `103`). It's the same command but flags completely change its behavior.
- **Piping (`ls -la | head -n 4`):** The `|` symbol takes the output of the command on the left and feeds it straight into the command on the right. So `ls -la` lists everything, and `head -n 4` only keeps the first 4 lines. No temporary file needed — it's like connecting two garden hoses.

### Task 2.4 — Package managers
I checked Homebrew (didn't install or remove anything):
- `brew --version` → `Homebrew 7.0.9`
- `brew list --formula` → showed 22 packages including `git`, `ffmpeg`, `cowsay`

A package manager is basically like an app store for command-line tools. Instead of hunting down download links and installers, you just type `brew install <tool>` and it handles everything — downloading, installing, and even managing dependencies (other tools the main one needs to work). Way less painful than doing it manually.

## 3. Commands / tools used
`pwd`, `ls`, `ls -lah`, `cd`, `mkdir`, `touch`, `echo` with `>` and `>>`, `cat`, `cp`, `mv`, `|` (pipe), `head -n`, `brew --version`, `brew list`

## 4. My understanding
Terminal felt intimidating at first but it's actually faster than Finder for a lot of things once you get the hang of it. The idea of composing small commands together with pipes is clever — each command does one simple thing, but you can chain them to do complex stuff. And the flag system means you don't need a separate command for every variation — just slap on `-l` or `-a` to change the behavior.

## 5. Difficulties faced
When I saved the `ls -lah` output for my evidence file, I noticed my actual Mac username was showing up in the owner column of every single line.

## 6. How I resolved them
I went through the evidence file and replaced my username with `[redacted]` before committing. A bit tedious but necessary for a public repo.

## 7. Evidence / files
- [mission-02-terminal/terminal-practice/notes.txt](terminal-practice/notes.txt) — Two-line file created with `>` and `>>`
- [mission-02-terminal/terminal-practice/notes_archive.txt](terminal-practice/notes_archive.txt) — Renamed backup copy
- [mission-02-terminal/terminal-practice/sample.txt](terminal-practice/sample.txt) — Empty file from `touch`
- [evidence/mission-02-terminal-output.txt](../evidence/mission-02-terminal-output.txt) — Redacted Terminal outputs

## 8. Commit details
- **Message:** `Complete Terminal and file management mission`
- Committed on `main` and pushed to GitHub.
