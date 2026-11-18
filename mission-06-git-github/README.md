# Mission 6 — Git and GitHub

## 1. Task / objective
Understand the core Git version-control workflow, explain the difference between staging and committing, create a feature branch (`update-about`) to add a `"My Learning"` section to the root `README.md`, prepare a Pull Request workflow on GitHub, and build a personal Git command glossary.

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| --- | --- |
| Check repository status (`git status`) | Shows which branch I am currently on, which files have been edited or newly created, and which changes are staged and ready to commit. |
| Stage selected changes (`git add <file>`) | Places specific modified or new files into the staging area (index) so I can choose exactly what goes into the next snapshot. |
| Create a commit (`git commit -m "..."`) | Permanently saves a snapshot of everything currently in the staging area into the local repository history along with a descriptive message. |
| View commit history (`git log --oneline`) | Lists past commits in reverse chronological order with their short IDs and messages so I can review how the project evolved. |

**Difference between staging a change (`git add`) and committing it (`git commit`):**
Staging is a *preparation step*—like placing specific items into a box before sealing it. You can still unstage or add more files without changing the project's saved history. Committing *seals and records* that box permanently as a numbered checkpoint in Git's history so you can inspect, share, or return to that exact state later.

---

### Task 6.2 — Create and use a branch
1. Created and switched to a new branch named `update-about` using `git switch -c update-about`.
2. Edited the root `README.md` to add a `"My Learning"` section highlighting three key skills learned across earlier missions (Terminal usage, OS inspection, and number systems/encoding).
3. Verified the modified file with `git status`, staged it with `git add README.md`, and committed it with `"Add My Learning section to root README"`.
4. Switched back to `main` (`git switch main`) while keeping `update-about` ready to push to GitHub (`git push -u origin update-about`).

---

### Task 6.3 — Create a Pull Request
- **What a branch is:** A branch is an independent line of development copied from an existing commit (such as `main`). Changes made on a branch stay isolated so the main version of the project stays clean and working while new edits are drafted or tested.
- **What a Pull Request (PR) is:** A Pull Request on GitHub is a formal proposal asking to merge changes from one branch (here, `update-about`) into another branch (here, `main`). It displays a clear side-by-side diff of every modified line and gives teammates or reviewers a place to comment, suggest fixes, or approve before merging.
- **Why branches and Pull Requests are useful in team projects:** When multiple people work on the same repository, branches prevent teammates from overwriting each other's unfinished work, and Pull Requests create a review checkpoint that catches bugs and documents *why* a change was made before it reaches `main`.
- **Current Pull Request status:** The `update-about` branch and its commit (`Add My Learning section to root README`) are created locally and prepared to push (`git push -u origin update-about`) and open as a Pull Request (`update-about` -> `main`) on GitHub. **PR merge status:** Kept open (not merged unless requested by the instructor), per Mission 6 Task 6.3 Step 5.

---

### Task 6.4 — Build your Git command glossary

| Git operation | Command | One-line explanation in my own words |
| --- | --- | --- |
| Initialise a repository | `git init` | Turns the current folder into a new Git repository by creating its hidden `.git` tracking directory. |
| Check status | `git status` | Displays the active branch along with untracked, modified, and staged files. |
| Stage changes | `git add <file>` | Marks chosen file edits to be included in the next commit. |
| Commit changes | `git commit -m "<msg>"` | Saves a permanent snapshot of staged changes into local Git history with an explanatory message. |
| View history | `git log --oneline` | Prints a compact list of past commits from newest to oldest. |
| Create or list branches | `git branch` / `git branch <name>` | Lists existing local branches or creates a new branch at the current commit. |
| Switch branches | `git switch <name>` (or `git checkout <name>`) | Moves the working directory to another branch so new work happens on that line of history. |
| Publish changes | `git push -u origin <branch>` | Uploads local commits on a branch to the remote repository on GitHub. |
| Retrieve remote changes | `git pull` | Downloads the latest commits from GitHub and merges them into the current local branch. |

## 3. Commands / tools used
- `git status` — Checked branch and modified files before staging.
- `git switch -c update-about` & `git switch main` — Created and navigated between branches.
- `git add README.md` & `git commit -m "..."` — Staged and committed the `"My Learning"` update on `update-about`.
- `git log --oneline --decorate` — Verified the commit history and branch pointers.
- `git branch` — Confirmed both `main` and `update-about` exist locally.

## 4. My understanding
Git gives me a safety net for every single project I work on. Because staging and committing are separate steps, I can keep each mission's commit focused and readable instead of mixing unrelated changes together. Branching (`update-about`) proved how easy it is to edit a file like `README.md` on a separate track while leaving `main` completely untouched until the change is reviewed via a Pull Request on GitHub.

## 5. Difficulties faced
Switching back to `main` after editing `README.md` on `update-about` initially felt surprising because the `"My Learning"` section disappeared from the file on `main`.

## 6. How I resolved them
Checking `git log --oneline --decorate` and `git branch` confirmed that the commit was safely preserved on `update-about`, demonstrating exactly how Git isolates branch changes until a Pull Request is merged.

## 7. Evidence / files
- [mission-06-git-github/README.md](README.md) — Git workflow table, branch & Pull Request explanations, PR status note, and 9-command Git glossary.
- [evidence/mission-06-git-output.txt](../evidence/mission-06-git-output.txt) — Terminal log of creating `update-about`, committing the README update, and inspecting `git log`.
- Branch `update-about` — Contains commit `Add My Learning section to root README`.

## 8. Commit details
- **Commit message (on `update-about`):** `Add My Learning section to root README`
- **Commit message (on `main`):** `Complete Git and GitHub collaboration mission`
- **Push status:** Both `main` and `update-about` are committed locally and ready to push to GitHub (`git push -u origin main` and `git push -u origin update-about`) to open the Pull Request.
