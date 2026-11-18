# Mission 1 — Know Your Computer

## 1. Task / objective
Understand how a computer takes in data, works on it, shows results, and saves things — this is called the IPOS model. Also identify hardware vs software items I actually use, and find computer-based systems in everyday life.

## 2. Work completed

### Task 1.1 — Tracing an activity using IPOS
I picked **typing and saving a document** as my activity.

| Stage | What happens | Hardware involved |
| --- | --- | --- |
| **Input** | I press keys on my keyboard to type notes, and hit `Cmd+S` to save | Keyboard, trackpad |
| **Processing** | The CPU converts each keystroke into character codes, holds the text in RAM, and checks spelling | CPU and RAM |
| **Output** | The letters appear on my screen in real time, and a save confirmation pops up | Display (and speakers if there's a notification sound) |
| **Storage** | The file gets written from temporary RAM to a permanent file on my SSD | Internal SSD |

The flow is basically: keyboard sends signals → CPU processes them in RAM → screen shows the result → SSD saves it permanently. When I hit save, that's actually another input that triggers the CPU to write from RAM to disk.

### Task 1.2 — Hardware and software I use

| Item | Hardware or software? | Software type | What I use it for |
| --- | --- | --- | --- |
| Built-in keyboard | Hardware | — | Typing text and shortcuts |
| Trackpad | Hardware | — | Moving the cursor, clicking, scrolling |
| Display | Hardware | — | Seeing everything on screen |
| SSD | Hardware | — | Storing files, apps, and the OS permanently |
| macOS | Software | Operating system | Manages the whole computer — memory, files, security, running apps |
| VS Code | Software | Application | Writing and editing code |
| Safari / Chrome | Software | Application | Browsing the web and using GitHub |
| Activity Monitor | Software | Utility | Checking which apps are using CPU and memory |

The distinction that helped me: **operating system software** runs the whole machine, **application software** is stuff I open to do specific tasks, and **utility software** is for maintenance and monitoring.

### Task 1.3 — Computer systems around me

| System | Main purpose | One input | One output |
| --- | --- | --- | --- |
| ATM | Withdraw cash or check balance | Inserting debit card and entering PIN | Dispensing cash and showing balance on screen |
| Metro ticket machine | Buy travel tickets | Selecting destination on touchscreen | Printing the ticket |
| Traffic signal controller | Manage traffic flow at intersections | Sensors detecting vehicles on the road | Changing the traffic lights |

## 3. Commands / tools used
Just my text editor for writing the tables, and `git add` / `git commit` to save the work.

## 4. My understanding
The IPOS cycle is everywhere — not just in laptops but also in ATMs, traffic lights, and ticket machines. They all take some kind of input, process it, produce an output, and store data. The hardware gives the physical parts, and software gives those parts instructions on what to do. I found it interesting that even something as "dumb" as a traffic light is actually a computer running the IPOS loop.

## 5. Difficulties faced
I got a bit confused between utility software and operating system software at first, since things like Activity Monitor and Disk Utility come pre-installed with macOS.

## 6. How I resolved them
I thought about it this way: macOS itself is what makes everything run — it manages memory, processes, hardware. But Activity Monitor is just a monitoring tool that sits on top of macOS. It doesn't manage resources, it just lets you *look at* them. That's what makes it a utility.

## 7. Evidence / files
- [mission-01-computer-basics/README.md](README.md) — All three tables and explanations

## 8. Commit details
- **Message:** `Complete computer basics and IPOS mission`
- Committed on `main` and pushed to GitHub.
