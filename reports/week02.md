# 📅 Week 2: [Bash, Make, Git, & Ruff]

## 🛠️ 1. What I Built
- **Summary**: I created a prep_data.sh script to automate data preprocessing and set up a Makefile to run tasks with simple commands like make prep and make clean. I also configured GitHub CLI authentication to resolve push issues and practiced using Ruff in VS Code to lint and auto-fix Python code style problems.
- **Key Tools Used**: WSL (Ubuntu), Makefile, Bash, Ruff, VS Code
- **Artifact Location**:
  - wsl records : https://www.notion.so/Week02-2671614c285f8006a9e5c688926237b1
  - exam2.py https://github.com/Sy-Lyy/MLOps-Practical-1.git

- **How to Run** (if applicable)
  - [o] Installation steps (if needed) : Install make (Linux: sudo apt install make)
  - [o] Run command(s) : Run make prep inside the scripts/ directory
  - [o] Expected output : a data directory is created, the iris dataset is downloaded, one synthetic row is added, and the total number of rows is reported

## 🔍 2. My Exploration
- **What I Investigated Further**:
  - I configured Ruff using pyproject.toml. At first I put select and ignore under [tool.ruff], but Ruff showed a deprecation warning and I fixed it by moving them to [tool.ruff.lint]. Running ruff check exam2.py then showed “All checks passed!”.
  - I also asked ChatGPT: “Why is it beneficial to keep Ruff settings inside the project itself?”
    - Summary of the answer: Keeping Ruff settings in the project ensures consistency across developers, avoids long CLI flags, integrates better with IDEs, makes style rules version-controlled, and guarantees reproducibility in CI pipelines.
- **Link to Evidence**
- exam2.py https://github.com/Sy-Lyy/MLOps-Practical-1.git, Terminal : https://www.notion.so/Exam2-Terminal-2671614c285f805a87c8e720d577a771

## 🤖 3. Use of GenAI (if applicable)
- **What I Asked It To Do**:
  - ## GenAI Usage Log
- 2025-09-05: Asked ChatGPT how to run sudo apt update, sudo apt install gh, and gh auth login in a WSL (Ubuntu) environment.
- 2025-09-05: Asked ChatGPT how GitHub CLI device code authentication works, and what to do when the browser does not automatically open in WSL.
- 2025-09-05: Asked ChatGPT about the difference between installing tools with pip and apt in Ubuntu, and how to adapt these steps compared to an initial Docker-based setup.

- **What I Got and Did With It**:
  - Learned that GitHub no longer supports password authentication, and that Personal Access Tokens or GitHub CLI authentication must be used instead.
  - Installed GitHub CLI with sudo apt install gh and successfully logged in using gh auth login with the browser device code method.
  - Verified that after authentication, git push origin main worked successfully.
- **Risks or Misuses You Noticed**:
  - I noticed that relying on ChatGPT for installation and authentication steps could unintentionally expose sensitive setup information. For example, sharing terminal outputs containing device codes or authentication URLs might compromise security if copied or logged elsewhere. I also realized that following AI instructions that differ from my existing Docker setup could cause version inconsistencies between local and container environments.
## 💬 4. Reflection
- **How did this week’s work support reproducibility or deployment?** : By creating a prep_data.sh script with a Makefile, I automated data preparation so it can be repeated easily.
- **What was most confusing or interesting?** : I was confused about the file save locations, which caused the data not to appear properly. I realized that errors often come not from complex code but from small mistakes like this, and I learned that I need to pay more attention to these basic details.
- **If someone else looked at your repo, what would help them use this part of the project?** : If someone else looked at my repo, it would help them if I included clear instructions on how to run the prep_data.sh script with the Makefile, how to set up GitHub CLI authentication for pushing changes, and how to use Ruff with the provided pyproject.toml settings.
