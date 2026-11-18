# The Digital Detective (`digital-detective-8532`)

## About This Assignment
**The Digital Detective** is an independent learning assignment designed to explore how a computer works from the inside out. Across nine structured missions, this repository documents hands-on investigations into computer fundamentals (IPOS), Terminal file management, operating system concepts, program execution, number systems and text encoding, Git/GitHub collaboration, and computer networking.

> **Workflow note:** Each mission is completed in order, documented inside its own folder with a standardized `README.md`, and committed separately to Git before moving on to the next mission. No personal or sensitive system/network details are published in this repository.

## Mission Index

| Mission | Focus Area | Documentation |
| --- | --- | --- |
| Mission 0 | Repository and workspace setup | [mission-00-setup/README.md](mission-00-setup/README.md) |
| Mission 1 | Computer fundamentals and IPOS | [mission-01-computer-basics/README.md](mission-01-computer-basics/README.md) |
| Mission 2 | Terminal and file management | [mission-02-terminal/README.md](mission-02-terminal/README.md) |
| Mission 3 | Operating system, processes and permissions | [mission-03-operating-system/README.md](mission-03-operating-system/README.md) |
| Mission 4 | How programs run | [mission-04-programs/README.md](mission-04-programs/README.md) |
| Mission 5 | Number systems, Python and text encoding | [mission-05-numbers-data/README.md](mission-05-numbers-data/README.md) |
| Mission 6 | Git, GitHub, branches and Pull Requests | [mission-06-git-github/README.md](mission-06-git-github/README.md) |
| Mission 7 | Computer networks | [mission-07-networking/README.md](mission-07-networking/README.md) |
| Mission 8 | Final review and submission | [mission-08-final-report/README.md](mission-08-final-report/README.md) |

## Topics Explored
- **Computer Fundamentals & IPOS:** Input, Processing, Output, Storage cycle; hardware vs. OS/application/utility software; everyday embedded computer systems.
- **Terminal & File Management:** Navigating paths (`pwd`, `cd`, `ls`), safe file creation/editing (`mkdir`, `touch`, `>`, `>>`, `cp`, `mv`, `cat`), flags (`-lah`), pipes (`|`), and inspecting Homebrew.
- **Operating Systems:** macOS/Darwin architecture, storage monitoring (`df -h`), running processes and PIDs (`ps`, `top`), absolute vs. relative paths, `rwx` file permissions, and core OS responsibilities.
- **How Programs Run:** Executing Python scripts from Terminal (`hello.py`) and comparing compilers vs. interpreters.
- **Number Systems & Text Encoding:** Manual and Python-verified conversions across decimal, binary, and hexadecimal; building a Python converter; ASCII vs. UTF-8 character representation.
- **Git & GitHub Collaboration:** Staging vs. committing, commit history inspection, branching (`update-about`), Pull Requests, and a 9-command Git glossary.
- **Computer Networks:** LAN/MAN/WAN, DNS, routers, protocols, packet switching, client-server architecture, `ping`/`nslookup` observations, and how websites load end-to-end.

## How to Run the Number Converter
Run the Mission 5 Python number converter directly from its mission folder in Terminal:

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

Enter any decimal integer (for example `13`, `25`, `42`, or `255`), and the program prints its binary (`0b...`) and hexadecimal (`0x...`) representations.

## Summary of What I Learned
Building this mini system report connected ideas that previously felt separate. Seeing how keystrokes flow through IPOS, how Terminal commands interact directly with the macOS operating system, how numbers and text map to bits, how Python executes code, how Git tracks versions safely across branches, and how DNS and packets deliver websites gave me a clear end-to-end mental model of modern computing.

## Supporting Folder
- [evidence/](evidence/README.md) — Privacy-safe command outputs grouped by mission.
