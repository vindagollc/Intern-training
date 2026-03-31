
## Phase 1: Branching Strategy (The Foundation)
Before writing code, interns must understand **where** that code lives. We use the **GitHub Flow** model for its simplicity and speed.

* **The Golden Rule:** The `main` branch is always deployable. Never commit directly to it.
* **Feature Branches:** Every task gets its own branch. 
    * *Naming Convention:* `feature/description` or `bugfix/issue-number`.
* **Context Switching:** Use `git checkout -b <branch-name>` to create a new "parallel universe" for your work.



---

## Phase 2: The Logic of Rebase vs. Merge
This is where most interns get tripped up. It's helpful to think of it as **preserving history** vs. **rewriting history.**

### The Merge Strategy
* **What it is:** A non-destructive operation that creates a "merge commit" to tie two histories together.
* **When to use it:** When finishing a feature and moving it into `main`.
* **The Vibe:** "I want everyone to see exactly when and how these branches joined."

### The Rebase Logic
* **What it is:** Moving your entire branch so it begins at the tip of the latest `main` commit.
* **When to use it:** To keep your feature branch up-to-date while you're still working on it.
* **The Vibe:** "I want my history to look like a perfectly straight line, as if I started my work today."



---

## Phase 3: Pull Requests (PRs) & Approvals
A PR isn't just a request to merge; it’s a **conversation** and a quality gate.

1.  **Draft PRs:** Open a PR early as a "Draft" to show progress and get early feedback.
2.  **The Description:** Always include *What* changed, *Why* it changed, and *How* to test it.
3.  **The Review Cycle:** * Address comments using "Suggestions" in GitHub.
    * **Approval Policy:** We require at least one (or two) approvals from senior devs before the "Merge" button turns green.
    * **CI/CD:** Ensure all automated tests (GitHub Actions) pass before requesting a review.

---

## Phase 4: Practical "Safe" Exercises
To get comfortable, I recommend interns perform these steps in a "Sandbox" repository:

* **Task A:** Create a branch, make a change, and open a PR.
* **Task B:** Simulate a **Merge Conflict** by having two interns edit the same line of a file, then resolve it together.
* **Task C:** Practice a `git rebase main` on a feature branch to see how the commit hashes change.

---

### Suggested Learning Timeline

| Day | Topic | Key Command |
| :--- | :--- | :--- |
| **Day 1** | Branching & Commits | `git checkout -b`, `git commit -m` |
| **Day 2** | Remote Work | `git push`, `git fetch`, `git pull` |
| **Day 3** | PRs & Code Review | GitHub UI Navigation |
| **Day 4** | Advanced Logic | `git rebase`, `git stash`, `git merge --squash` |

> **Pro-Tip:** If you ever get stuck in a "detached HEAD" state or a messy rebase, don't panic. `git rebase --abort` is your best friend—it's like a cosmic "undo" button.