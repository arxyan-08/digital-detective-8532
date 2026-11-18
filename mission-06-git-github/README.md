# Mission 6 — Git and GitHub

## 1. Task / objective
Understand the core Git workflow (staging, committing, viewing history), create a branch, prepare a Pull Request, and build a personal Git command glossary.

## 2. Work completed

### Task 6.1 — Basic Git workflow

| Git operation | What it does |
| --- | --- |
| `git status` | Shows which branch I'm on and which files have been changed, added, or are ready to commit |
| `git add <file>` | Puts a file into the "staging area" — like packing items into a box before sealing it |
| `git commit -m "..."` | Seals the box — permanently saves everything that's staged as a snapshot in Git history |
| `git log --oneline` | Lists past commits from newest to oldest with their short IDs and messages |

**Staging vs committing — what's the difference?**
Staging (`git add`) is a preparation step. You're choosing which files go into the next snapshot. You can still change your mind, unstage things, or add more. Committing (`git commit`) is when you actually lock it in — it creates a permanent checkpoint in your project's history with a message describing what changed.

### Task 6.2 — Creating and using a branch
1. Created a new branch: `git switch -c update-about`
2. Added a "My Learning" section to the root `README.md` with three key things I learned across earlier missions
3. Staged and committed: `git add README.md` → `git commit -m "Add My Learning section to root README"`
4. Switched back to `main`: `git switch main`

The cool part? After switching back to `main`, the "My Learning" section *disappeared* from the README. It's not deleted — it's safely sitting on the `update-about` branch. That's exactly how branches are supposed to work.

### Task 6.3 — Pull Request
- **What's a branch?** An independent copy of your project where you can make changes without affecting `main`. Like working on a draft in a separate notebook.
- **What's a Pull Request?** A formal way of saying "hey, I made some changes on this branch — please review them before merging into `main`." On GitHub, it shows a side-by-side comparison of what changed and lets people leave comments.
- **Why they matter for teams:** When multiple people work on the same repo, branches keep everyone's unfinished work separate. PRs create a checkpoint where someone can review the changes before they reach `main`, catching bugs and mistakes early.

The `update-about` branch is pushed to GitHub and the PR (`update-about` → `main`) has been created. Keeping it open unless the instructor says to merge.

### Task 6.4 — Git command glossary

| What you want to do | Command | What it does |
| --- | --- | --- |
| Start a new repo | `git init` | Creates a hidden `.git` folder that turns your project into a Git repository |
| Check what's changed | `git status` | Shows modified, staged, and untracked files plus your current branch |
| Stage files | `git add <file>` | Marks files to be included in the next commit |
| Save a snapshot | `git commit -m "..."` | Records staged changes permanently with a description |
| See past commits | `git log --oneline` | Lists the commit history in a compact format |
| Create a branch | `git branch <name>` | Makes a new branch starting from the current commit |
| Switch branches | `git switch <name>` | Moves your working directory to another branch |
| Push to GitHub | `git push -u origin <branch>` | Uploads your local commits to the remote repository |
| Pull from GitHub | `git pull` | Downloads and merges the latest changes from the remote |

## 3. Commands / tools used
`git status`, `git switch -c update-about`, `git switch main`, `git add`, `git commit -m "..."`, `git log --oneline --decorate`, `git branch`, `git push`

## 4. My understanding
Git is basically a time machine for your code. The staging area gives you control over exactly what goes into each commit, so you can keep commits focused and clean. Branching felt a bit abstract until I actually saw the "My Learning" section disappear when I switched back to `main` — that made it click. It's not gone, it's just on a different timeline.

## 5. Difficulties faced
When I switched back to `main` after editing the README on `update-about`, it was initially confusing to see the changes vanish from the file.

## 6. How I resolved them
I ran `git log --oneline --decorate` and `git branch` to confirm both branches existed and the commit was safely preserved on `update-about`. That proved Git was working exactly as intended — changes are isolated to their branch until merged.

## 7. Evidence / files
- [mission-06-git-github/README.md](README.md) — Workflow table, branch/PR explanation, and glossary
- [evidence/mission-06-git-output.txt](../evidence/mission-06-git-output.txt) — Terminal log of branch creation, committing, and log inspection
- Branch `update-about` on GitHub with its Pull Request

## 8. Commit details
- **Message (on `update-about`):** `Add My Learning section to root README`
- **Message (on `main`):** `Complete Git and GitHub collaboration mission`
- Both pushed to GitHub.
