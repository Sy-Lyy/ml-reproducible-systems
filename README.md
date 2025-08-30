[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20227413&assignment_repo_type=AssignmentRepo)
# rs-rmd-portfolio-template
Template for the portfolio assignment of the course RS: Reproducibility &amp; Model Deployment.

**‼️ NOTE**: you can delete the contents of this file. This is just to get you started!

### 🗂️ Quick tour of the **non-code files** in your starter repo

Below we'll tell you what each file does, why you should care, and when we’ll meet it in class.

| 🗄️ File / Folder                | 💡 What it is                                                        | 🙏 Why you’ll be glad it’s there                                                    | 🔎 When we’ll zoom in on it                                      |
| ------------------------------ | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **`README.md`**                | Your project’s front door; first place visitors land.                | Lets anyone (future-you included) clone the repo and run the code without guessing. | **Week 1** We draft the first version together.                 |
| **`LICENSE`**                  | The permission slip for using and sharing your code.                 | Makes it crystal-clear what others can (and can’t) do with your work.               | **Week 1** Comes pre-filled; we explain why it matters.         |
| **`CITATION.cff`**             | A machine-readable “cite me” card.                                   | Helps scholars give you credit; GitHub even shows a “Cite this repo” button.        | **Week 1** Tiny file, big academic karma.                       |
| **`.gitignore`**               | The repo’s bouncer.                                                  | Keeps huge data files, secrets, and temp junk out of version control.               | **Week 1** You’ll tweak it when odd files slip through.         |
| **`pyproject.toml`**           | Python’s modern shopping list for dependencies and packaging info.   | Guarantees teammates and CI install the **same** versions.                          | Intro **Week 1**, extended in **Week 2** when we add real libs. |
| **`requirements.txt`**         | A lighter, classic dependency list—express checkout.                 | Quick install for people who don’t use `pyproject` yet.                             | **Week 2** We pin versions later for full reproducibility.      |
| **`environment.yml`**          | A Conda recipe card (optional).                                      | Cross-platform fall-back if you prefer Conda to `venv`.                             | **Week 2** Optional exercise.                                   |
| **`Makefile`**                 | Your repo’s*remote control (`make test`, `make run`).                | One-liners save you from remembering long commands.                                 | **Week 2** We add tasks as the project grows.                   |
| **`Dockerfile`**               | A shipping container spec—bundles OS + code + deps.                  | “Works on my machine” now means “works everywhere.”                                 | **Week 4** Containerisation week.                               |
| **`.github/workflows/ci.yml`** | The repo’s robot tester (Continuous Integration).                    | Runs your tests on every push so broken code never sneaks in.                       | **Week 3** Right after you write real tests.                    |
| **`tests/`**                   | Your safety net; pytest files live here.                             | Catch bugs early; prove your pipeline still works months later.                     | **Week 3** We’ll turn the smoke test into real coverage.        |
| **`data/` (+ a small README)** | The parking lot for raw or processed data (mostly not in Git).       | Documents exactly where to fetch data without bloating the repo.                    | **Week 5** Data-pipeline week.                                  |
| **`notebooks/`**               | Your scratchpad for quick experiments / EDA.                         | Keeps exploratory work separate from production code.                               | Mentioned **Week 3** when we talk tidy notebooks.               |
| **`deployment/`**              | The showroom; Streamlit or FastAPI app plus configs.                 | Turns your model into something people can click on.                                | **Week 6** Deployment week.                                     |
| **`reports/`**                 | Your weekly journal.                                                 | Captures what you tried, learned, and how (or if) you used GenAI.                   | **Every week**—first entry in Week 1.                           |

Use this table whenever you wonder, “Wait, what’s that file for again, and why did you make me keep it?”
It’s all about making your work reproducible, shareable, and future-proof; exactly the skills this course is designed to build.
