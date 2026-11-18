# Mission 0 — Setting Up the Workspace

## 1. Task / objective
Create a properly named repository (`digital-detective-8532`) on my computer, check that Python and Git are installed, set up all the mission folders and files, and connect it to GitHub.

## 2. Work completed
I picked the name `digital-detective-8532` following the naming rule (assignment name + last 4 digits of my USN). Then I checked my tools in Terminal:
- `python3 --version` gave me `Python 3.13.15` — good to go
- `git --version` showed `git version 2.56.0` — also fine

After that I created the main project folder and all the subfolders for missions 0 through 8, plus an `evidence/` folder for storing Terminal output screenshots later. I also made empty starter `README.md` files in each mission folder and an empty `number_converter.py` in the mission-05 folder since I knew I'd need it later.

I set up Git with `git init -b main`, added the GitHub remote URL, and configured a noreply email so my personal Mac username wouldn't show up in public commits.

## 3. Commands / tools used
- `python3 --version` and `git --version` to check everything was installed
- `mkdir -p` to create all the folders in one go
- `touch` to create the empty starter files
- `git init -b main` to start the repo on the `main` branch
- `git config` to set a privacy-safe author name and email
- `git remote add origin` to link it to GitHub
- `git add .` and `git commit` to save the initial structure

## 4. My understanding
A repository is basically a project folder that Git watches over — it tracks every change I make so I can go back in time if something breaks. I organized it into separate folders per mission because it keeps things clean and makes it easy to find stuff later, especially on GitHub where someone else might browse through it.

## 5. Difficulties faced
Two small things tripped me up. First, Git doesn't track empty folders — so if I just made `evidence/` with nothing in it, it wouldn't show up on GitHub. Second, I realized the default Git config would use my Mac's local username and device name in every commit, which would be visible publicly.

## 6. How I resolved them
For the empty folder issue, I just added a small `README.md` inside `evidence/` explaining what the folder is for. For the privacy thing, I set up a repository-level Git config with the GitHub noreply email address instead.

## 7. Evidence / files
- [Root README.md](../README.md)
- [evidence/README.md](../evidence/README.md)
- `.gitignore` (keeps `.DS_Store` and Python cache out of commits)

## 8. Commit details
- **Message:** `Set up Digital Detective mission structure`
- Committed on `main` and pushed to GitHub.
