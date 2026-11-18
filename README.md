# The Digital Detective — `digital-detective-8532`

Hey! This is my Diwali Independent Learning Assignment where I explored how my computer actually works under the hood. Across 9 missions, I dug into everything from how keystrokes become text on screen, to what actually happens when I open a website.

Each mission is in its own folder and was completed and committed one at a time before moving to the next.

## Mission Index

| Mission | What it covers | Link |
| --- | --- | --- |
| 0 | Setting up the repo and folders | [mission-00-setup/README.md](mission-00-setup/README.md) |
| 1 | IPOS and computer basics | [mission-01-computer-basics/README.md](mission-01-computer-basics/README.md) |
| 2 | Getting comfortable with Terminal | [mission-02-terminal/README.md](mission-02-terminal/README.md) |
| 3 | How macOS manages everything | [mission-03-operating-system/README.md](mission-03-operating-system/README.md) |
| 4 | Running Python and compiler vs interpreter | [mission-04-programs/README.md](mission-04-programs/README.md) |
| 5 | Number systems, Python converter, and text encoding | [mission-05-numbers-data/README.md](mission-05-numbers-data/README.md) |
| 6 | Git branching and Pull Requests | [mission-06-git-github/README.md](mission-06-git-github/README.md) |
| 7 | Networking — what happens when you open a website | [mission-07-networking/README.md](mission-07-networking/README.md) |
| 8 | Final check and submission | [mission-08-final-report/README.md](mission-08-final-report/README.md) |

## Topics I Explored
- How the IPOS cycle works (Input → Processing → Output → Storage) and the difference between hardware, OS software, apps, and utilities
- Terminal basics — navigating folders, creating/copying/renaming files, using flags like `-lah`, and piping output with `|`
- What macOS does behind the scenes — processes, PIDs, storage, file permissions (`rwx`), and OS responsibilities
- Writing and running a Python script (`hello.py`) and understanding how compilers differ from interpreters
- Converting between decimal, binary, and hexadecimal by hand, verifying with Python, and building a small converter program
- Git workflow — staging vs committing, branching, Pull Requests, and a command glossary
- Networking — LAN/WAN/DNS, routers, protocols, packet switching, and tracing what happens step by step when a website loads

## How to Run the Number Converter
```bash
cd mission-05-numbers-data
python3 number_converter.py
```
Type in any whole number (like `42`) and it shows the binary and hex versions.

## What I Took Away From This
Honestly, before this assignment I never really thought about what happens between pressing a key and seeing a letter show up. Now I can trace that whole journey — from the keyboard sending a signal, to the CPU processing it, to the screen displaying it, to the SSD saving the file. Same thing with opening a website — it's not magic, it's DNS lookups, routers forwarding packets, and servers sending back HTML. Connecting all these pieces into one mental picture was probably the most useful part of this whole project.

## Other
- [evidence/](evidence/README.md) — Redacted Terminal outputs used as proof for different missions
- Every mission was documented and committed separately before starting the next one
