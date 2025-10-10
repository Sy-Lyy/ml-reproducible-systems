# 📅 Week 1: [Git hub]

## 🛠️ 1. What I Built
- **Summary**: I practiced the core Git workflow in VS Code: editing files, staging, committing, and pushing changes to GitHub. I also pulled updates from GitHub to my local repo, linked a commit to an issue so it closed automatically, and created a new branch to make changes and open a pull request, which I then merged into main I also explored undo and recovery commands, such as git restore to revert files and git reflog to recover lost commits.
- **Key Tools Used**: VS Code, Git hub
- **Artifact Location**: [README.md] https://github.com/Sy-Lyy/MLOps-Practical-1/blob/main/README.md [Branch] 1. fun-fact : https://github.com/Sy-Lyy/MLOps-Practical-1/pull/2 2. rescue-branch : https://github.com/Sy-Lyy/MLOps-Practical-1/compare/rescue-branch?expand=1 [Issues] https://github.com/Sy-Lyy/MLOps-Practical-1/issues/1

- **How to Run** (if applicable)
  - [ ] Installation steps (if nded)
  - [ ] Run command(s)
  - [ ] Expected output

## 🔍 2. My Exploration
- **What I Investigated Further**:
  - To practice recovering a specific file, I created a new test repository and tried reverting and restoring changes in the working directory (unstaged), as well as checking whether the recovery worked properly. I explored canceling only the staging or reverting both the staging and the content, and also tested restoring a file after it was deleted—both before and after committing it. To simulate losing a commit, I created one, reset it by mistake so it was lost, and then used reflog to find the missing commit. I learned different ways of recovering it, including fully restoring to that point, reviving it by creating a new branch, and applying it with cherry-pick. In practice, I only tried the method of reviving it with a new branch.
- **Link to Evidence** rescue-branch : https://github.com/Sy-Lyy/MLOps-Practical-1/compare/rescue-branch?expand=1

## 🤖 3. Use of GenAI (if applicable)
- **What I Asked It To Do**:
  - ## GenAI Usage Log
- 2025-08-30: Asked ChatGPT what the code Update README with intro draft (see #1) means.
- 2025-08-30: Asked ChatGPT to show me how to create a new file and make a commit.
- 2025-08-30: Asked ChatGPT how to recover changes or restore a specific file.
- 2025-08-30: Asked ChatGPT how to find and recover a lost commit.
- **What I Got and Did With It**:
  - I checked what the commit message Update README with intro draft (see #1) means in GitHub workflow.
  - I modified files in the working directory and then verified how to revert and recover them.
  - I checked the difference between canceling only staging and reverting both staging and file content.
  - I deleted files and verified recovery both before and after committing them.
  - I simulated losing a commit, then verified how to find and restore it using reflog.
  - I confirmed that I could recover a lost commit by creating a new branch
- **Risks or Misuses You Noticed**:
  - There were no issues.

## 💬 4. Reflection
- **How did this week’s work support reproducibility or deployment?** : Using Git and VS Code together helped me see how version control tools support reproducibility by keeping track of every change, and verifying lost commit recovery with reflog increased my confidence that important progress can always be restored
- **What was most confusing or interesting?** : I got a bit confused when trying to upload the rescue branch I had created locally to GitHub. On one hand, I learned that I could create a branch after cloning my GitHub repository locally, and on the other hand, I was shown how to push a new branch directly to the remote. One of the commands was not very clear to me, but overall I found it interesting to see how VS Code and GitHub integrate and work together. I also realized that even if a command looks confusing at first, experimenting step by step makes the workflow clearer. This exercise gave me a stronger sense of how version control tools are connected, and I found it satisfying to watch my edits in VS Code show up on GitHub right away.
- **If someone else looked at your repo, what would help them use this part of the project?** : Clear commit messages that explain what was changed and why.

