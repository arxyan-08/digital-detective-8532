# Mission 1 — Know Your Computer

## 1. Task / objective
Explain how a computer receives input, processes data, produces output, and stores results using the IPOS model; classify real hardware and software items I use every day; and identify computer-based systems in everyday life beyond laptops and phones.

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
**Chosen activity:** Typing, spell-checking, and saving a study summary document in a text editor.

| Stage | What happens in your example? | Possible hardware / component |
| --- | --- | --- |
| **Input** | I press keys to type my study notes, click buttons to format headings, and press `Command + S` when I want to save the document. | Keyboard and trackpad / mouse |
| **Processing** | The processor turns each keystroke into character codes, holds the active text in RAM, checks spelling and formatting rules, and prepares the file data for saving. | CPU (processor) and RAM (memory) |
| **Output** | The typed characters, bold headings, and spelling underlines appear immediately on the screen, and a brief save confirmation shows in the editor window. | Display / monitor (and speakers if a notification sound plays) |
| **Storage** | When I save, the file is written permanently from temporary RAM into a saved `.md` or `.txt` file on disk so it remains available after restarting the computer. | Internal SSD (and optionally GitHub / cloud storage when backed up) |

**How the activity moves through IPOS (with extra steps):**
1. **Input -> Processing:** Pressing a key sends an electrical signal to the CPU, which converts it into digital data stored temporarily in RAM.
2. **Processing -> Output:** The editor program and graphics hardware immediately draw the new letters on the screen so I can see what I typed in real time.
3. **Second Input -> Processing -> Storage:** Pressing `Command + S` is another input; the CPU packages the current document from RAM and instructs the SSD controller to save those bytes permanently to a file inside my folder.
4. **Feedback Output:** The editor updates the window title (removing the "unsaved" dot) on the screen to confirm the file is safely stored.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| --- | --- | --- | --- |
| Built-in keyboard | Hardware | Not applicable | Sends typed letters, numbers, and shortcuts into the computer. |
| Trackpad | Hardware | Not applicable | Controls the on-screen pointer for clicking, scrolling, and selecting items. |
| Display screen | Hardware | Not applicable | Visually shows the desktop, text, apps, and command outputs. |
| Solid-State Drive (SSD) | Hardware | Not applicable | Permanently stores the operating system, applications, and personal files even when powered off. |
| Processor (CPU) | Hardware | Not applicable | Performs calculations, runs instructions, and coordinates all tasks. |
| macOS | Software | Operating system software | Manages hardware resources, memory, files, security, and lets other programs run. |
| Visual Studio Code (VS Code) | Software | Application software | Used to write, edit, and organize code and Markdown documents. |
| Web browser (Safari / Chrome) | Software | Application software | Used to access websites, documentation, and GitHub. |
| Activity Monitor | Software | Utility software | Monitors running processes, CPU usage, and memory consumption to help diagnose slowdowns. |
| Disk Utility | Software | Utility software | Checks disk health, manages storage volumes, and repairs drive errors. |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| --- | --- | --- | --- |
| **Automated Teller Machine (ATM)** | Allows bank customers to withdraw cash, check balances, or transfer money securely without a teller. | Inserting a debit card and entering a PIN on the keypad. | Dispensing banknotes and displaying the updated balance on the screen (or printing a receipt). |
| **Metro Ticket Vending Machine** | Issues travel tickets or recharges smart cards for commuters at transit stations. | Selecting the destination station on the touchscreen and tapping a payment card or inserting cash. | Printing a QR paper ticket / recharging the smart card and showing confirmation on the screen. |
| **Automated Traffic Signal Controller** | Controls road intersections safely by timing green, yellow, and red lights to manage traffic flow. | Vehicle presence detected by road sensors or a pedestrian pressing the crosswalk button. | Changing the traffic lights and pedestrian walk/don't-walk signs. |

## 3. Commands / tools used
- **Text editor / Markdown:** Used to organize the IPOS trace and classification tables clearly.
- **Git (`git status`, `git add`, `git commit`):** Used to track and commit only the completed Mission 1 documentation.

## 4. My understanding
Every computer—whether a laptop, an ATM, or a traffic controller—follows the same core **IPOS (Input, Processing, Output, Storage)** cycle. Hardware provides the physical parts (like the keyboard, CPU, screen, and SSD), while software gives those parts instructions. Software itself has distinct roles: the **operating system** manages the whole machine, **application software** helps the user complete everyday tasks like coding or browsing, and **utility software** keeps the computer healthy and organized. Recognizing that everyday devices around us are also specialized computer systems makes it easier to understand how inputs turn into useful real-world actions.

## 5. Difficulties faced
Distinguishing between **operating system software** and **utility software** took a moment of thought because macOS ships with built-in utilities like Activity Monitor and Disk Utility.

## 6. How I resolved them
I separated the core role of each tool: macOS itself coordinates hardware and runs all programs (operating system software), whereas Activity Monitor and Disk Utility focus specifically on monitoring and maintaining the system (utility software).

## 7. Evidence / files
- [mission-01-computer-basics/README.md](README.md) — Contains all three completed tables (Tasks 1.1, 1.2, and 1.3) and the IPOS flow explanation.

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Push status:** Committed on `main` (staged and committed separately from Mission 0; ready to push to GitHub).
