# Mission 0 — Create Your GitHub Workspace

## 1. Task / objective
Create a properly named local project folder (`digital-detective-8532`), verify that Python 3 and Git are installed, build the required mission folder and file structure, prepare the root `README.md`, and connect the local Git repository to GitHub so every mission can be tracked cleanly.

## 2. Work completed
- Chose the repository name `digital-detective-8532` using the rule `digital-detective` + hyphen + last four digits of USN (`8532`).
- Checked that both Python 3 and Git are installed and working in Terminal:
  - **Python 3:** `Python 3.13.15`
  - **Git:** `git version 2.56.0`
- Created the local project directory `digital-detective-8532` and initialized a Git repository on the `main` branch.
- Created all required folders and starter files:
  - `README.md` (root project introduction and mission index)
  - `mission-00-setup/README.md`
  - `mission-01-computer-basics/README.md`
  - `mission-02-terminal/README.md`
  - `mission-03-operating-system/README.md`
  - `mission-04-programs/README.md`
  - `mission-05-numbers-data/README.md`
  - `mission-05-numbers-data/number_converter.py`
  - `mission-06-git-github/README.md`
  - `mission-07-networking/README.md`
  - `mission-08-final-report/README.md`
  - `evidence/README.md`
  - `.gitignore` (to prevent macOS `.DS_Store` and Python cache files from cluttering commits)
- Configured privacy-safe repository-local Git identity (`arxyan-08` and GitHub noreply address) and linked the `origin` remote to `https://github.com/arxyan-08/digital-detective-8532.git`.

## 3. Commands / tools used
- `python3 --version` — Verified that Python 3 is installed (`Python 3.13.15`).
- `git --version` — Verified that Git is installed (`git version 2.56.0`).
- `mkdir -p` — Created the repository folder and all mission subfolders cleanly in one step.
- `touch` — Created the empty starter Markdown files and `number_converter.py`.
- `git init -b main` — Initialized a new Git repository with `main` as the default branch.
- `git config` — Set a privacy-safe author name and noreply email for this repository.
- `git remote add origin` — Connected the local repository to the GitHub remote URL.
- `git add` & `git commit` — Staged and committed the initial repository structure.

## 4. My understanding
A **repository** is a project folder tracked by Git that stores both the current files and the full history of changes made to them over time. Organizing the repository into separate folders—one for each mission (`mission-00-setup` through `mission-08-final-report`) plus an `evidence/` folder—keeps each topic isolated, makes navigation easy for anyone reading the project on GitHub, and helps me review or fix one mission without accidentally disturbing another. Keeping personal information out of both files and Git commit metadata is also essential when working in a public repository.

## 5. Difficulties faced
Git does not track completely empty folders by default, so an empty `evidence/` folder would not appear on GitHub. Also, the default local computer email would have exposed my local username and device name in Git commits.

## 6. How I resolved them
Added a short `evidence/README.md` file inside `evidence/` so Git tracks the folder and explains its purpose, and configured a repository-local GitHub noreply email (`arxyan-08@users.noreply.github.com`) so no private computer details appear in commit history.

## 7. Evidence / files
- [Root README.md](../README.md)
- [evidence/README.md](../evidence/README.md)
- [mission-00-setup/README.md](README.md)
- `.gitignore`

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Push status:** Committed locally on `main` and ready to push to `https://github.com/arxyan-08/digital-detective-8532` once the empty public repository is created on GitHub.
