# Final Reflection — Reproducible Modeling Portfolio

**Python version: 3.11.x (recommended) — tested with Python 3.11**

This reflection summarizes six weeks of progressive work on building a **reproducible, testable, and deployable data science pipeline**.  
The project demonstrates how each reproducibility layer — from **Git tracking to Dockerized deployment** — integrates into one cohesive workflow.



## 1️⃣ Snapshot — What’s in this repo

| **Component** | **Description** | **Link / File** |
|----------------|-----------------|-----------------|
| **Git Versioning** | Branching, commit recovery (`reflog`, `reset`, `cherry-pick`) for traceable workflow. | [reports/week01.md](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week01.md) |
| **Automation (Makefile)** | Standardized commands (`prep`, `run`, `test`) to automate pipeline steps. | [Makefile](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/Makefile) |
| **Testing (pytest)** | Unit testing for `DataProcessor` class to verify deterministic logic. | [/tests/test_processor.py](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/processor.py) |
| **Environment Capture** | Portable environments via `requirements.txt`, `Dockerfile`, and Conda YAML. | [requirements.txt](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/requirements.txt), [Dockerfile](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/Dockerfile) |
| **Data Workflow** | Web scraping (BeautifulSoup) → cleaning → classification (pandas). | [/src/scrape_books.py](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/scrape_books.py) |
| **Deployment** | Model served through **FastAPI backend** and **Streamlit frontend**. | [/src/api.py](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/api.py), [/src/app.py](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/app.py) |
| **Reports** | Full weekly documentation of code, debugging, and learning process. | [/reports/](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/tree/main/reports) |



## 2️⃣ How to try it (demo commands)

## Overview
This demo builds and serves a complete text classification system, covering every step from web scraping, data cleaning, and model training to FastAPI deployment and Streamlit UI.
The entire workflow is reproducible through Docker and Makefile automation.


```powershell
# 1. Run the Makefile
# Install dependencies, Run pytest, Data collection, scraping, cleaning, train and classify
make all

# 2. Start FastAPI server
make run-api
# → Expected output: "Uvicorn running on http://127.0.0.1:8000"
# Keep this terminal open while testing endpoints.

# 3. Test endpoints (open a NEW PowerShell window)
Invoke-RestMethod "http://localhost:8000/health"
# Expected output: {"status": "RMD-OK"}
$body = @{ text = "the grand design" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/predict" -ContentType "application/json" -Body $body
# Expected output: "science"

# 4. Run Streamlit UI
streamlit run src/app.py
# → Open http://localhost:8501
# → Enter text and click "Predict" to see classification result.

# 5. Run via Docker for reproducibility demo (Open a new PowerShell window)
# Make sure Docker Desktop is running before running these commands.
docker build -t myapi .
docker run -p 8000:8000 myapi
# → Expected output: "Running experiment... Numpy version: 2.3.3"
```
---

## 3️⃣ Why these pieces matter (reproducibility in general)

| **Tool / Concept** | **Role in Reproducibility** | **Evidence** |
|---------------------|------------------------------|---------------|
| **Git** | Enables traceability and rollback (recover deleted commits). | [week1.md](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week01.md) |
| **Makefile** | Ensures consistent, automated execution across systems. | [Makefile](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/Makefile) |
| **pytest** | Detects logic errors early; makes results verifiable. | [week3.md](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week03.md) |
| **Docker** | Guarantees environment consistency; isolates dependencies. | [Dockerfile](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/Dockerfile) |
| **FastAPI + Streamlit** | Reproduces the same model behavior via a fixed API/UI interface. | [/src/api.py](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/api.py) |
| **Weekly Reports** | Contain step-by-step debugging logs for transparent reruns. | [/reports/](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/tree/main/reports) |
| **Ruff / Linting** | Maintains coding style and prevents hidden syntax issues. | [pyproject.toml](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/pyproject.toml) |
| **Determinism (random seeds)** | Ensures identical outputs across runs by fixing random processes (`random_state=42`). | Mentioned in [classify.py](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/classify.py) |

> **Together, these layers form a reproducibility stack** — from code versioning (**Git**) → automation (**Make**) → verification (**pytest**) → environment capture (**Docker**) → consistent delivery (**FastAPI / Streamlit**). In addition, all random components such as data splitting and model initialization were fixed with `random_state=42` to ensure deterministic reproducibility.


---

## 4️⃣ Deep Dives (topics explored further)

### Default Branch Fix (GitHub)
- **Challenge:** My GitHub repository’s default branch was mistakenly set to `feedback` instead of `main`
- **Fix:** After noticing that I didn’t have permission to change the default branch, I contacted the professor, who helped me resolve the issue.
  
---

### Pytest Test Discovery & Mean Calculation Bug
- **Challenge:** Unexpected test discovery in `pytest --collect-only`; miscalculated mean values.  
- **Fix:** Removed redundant test files, used debugger to verify variable states.  
- **Insight:** Testing isn’t only validation — it reveals hidden data logic flaws.  
- **Extend:** Integrate end-to-end functional tests for input→output verification.  
🔗 *See Week 3 report* https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week03.md

---

### Windows PowerShell ↔ API Request Standardization
- **Challenge:** FastAPI tests failed with `curl` due to PowerShell alias conflicts.  
- **Fix:** Replaced `curl` with `Invoke-RestMethod`, verified proper JSON output.  
- **Insight:** Even identical commands behave differently across OS; documentation of exact syntax is essential.  
- **Extend:** Keep platform-specific notes in README for first-time users.  
🔗 *See Week 6 report* https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week06.md

---

### WSL2 & Docker Daemon Issue
- **Challenge:** “Docker daemon not running” error when WSL2 backend stopped.  
- **Fix:** Restarted Docker Desktop after `wsl --shutdown`, logged every command.  
- **Insight:** Reproducibility includes OS-level dependencies, not just code.  
- **Extend:** Build OS-independent Compose setup for backend/frontend runtime.  
🔗 *See Week 4 report* https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week04.md

---

## 5️⃣ Peer Feedback 

| **Feedback from Peer** | **My Response** |
|--------------------------|-----------------|
| Add `requirements.txt` and specify Python version | Added `requirements.txt` after Week 5 (`pandas`, `scikit-learn`) and noted **Python 3.11 (recommended)** at the top of README for environment clarity. |
| Add docstrings and type hints for clarity | Added short docstrings and type hints to key functions (`DataProcessor.mean`, `scrape_books.parse_books_html`, `fetch_data.build_parser`) so argument types and outputs are immediately visible. |

| **Feedback Summary** | **Description** |
|------------------------|-----------------|
| Clear workflow recognition | I noted the strong and systematic workflow shown in Weeks 2–3, where Makefile automation and debugging practices clearly demonstrated reproducibility. |
| Improvement suggestion | Suggested adding a minimal README that includes environment setup steps and expected outputs so the repository can be more easily reproduced by others. |
| Overall impression | Highlighted steady learning progression from Git basics to automation, testing, and OOP; reflections were detailed and thoughtful. |
| Evidence | [Peer Feedback Issue #2](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/issues/2#issue-3438626303) |

---

## 6️⃣ GenAI — Used and Managed Transparently

**Purpose:** Used ChatGPT as a debugging assistant.

**Examples:**
- Converting `curl` → `Invoke-RestMethod` (Windows PowerShell)  
- Interpreting pytest errors & Ruff configuration  
- Explaining Docker build failures
- Generating a README template(Week 7)

**Risk Management:**
The summarized risks below are based on the weekly “Risks or Misuses You Noticed” sections documented under /reports/Use of GenAI.

- **Week 1**: Realized that running Git recovery or reset commands from ChatGPT without verifying context could risk data loss or overwriting local commits.
- **Week 2**: Learned that system-level commands like sudo apt install or authentication steps via GitHub CLI might alter permissions or environment settings if executed without care.
- **Week 3**: Found that AI-generated pytest examples sometimes mismatched the project structure, leading to missing or misleading test results.
- **Week 4**: Noted that mixing Conda, venv, and Poetry as suggested in different AI snippets could cause environment conflicts or version inconsistencies.
- **Week 5**: Understood that automatically generated Makefile or CLI automation from AI can reduce reproducibility and make debugging less transparent.
- **Week 6**: Experienced that combining FastAPI, Docker, and Streamlit following multi-layered AI steps could increase complexity and dependency overload without clear architectural understanding.

**Transparency:** All GenAI interactions logged under `/reports/Use of GenAI` sections.
- **Week 1–2**: Logged all Git and terminal troubleshooting prompts, showing how AI explanations were tested locally before inclusion in the report.
- **Week 3**: Recorded pytest and OOP debugging sessions, highlighting which parts of the code were AI-suggested and which were rewritten manually.
- **Week 4**: Noted environment-management commands and explicitly commented on differences between ChatGPT’s suggestions and verified Conda/Poetry outputs.
- **Week 5**: Documented how AI-generated Makefile rules and logging setup were adjusted for Windows PowerShell compatibility and reproducibility.
- **Week 6**: Included detailed prompts for FastAPI–Docker–Streamlit integration and noted where AI guidance was adapted, debugged, or replaced after testing.
---

## 7️⃣ If this became a “real” project — What next?
**Ris:**
Through this project, I was able to build a consistent, reproducible workflow that covered the entire process — from data collection to containerized deployment using FastAPI and Streamlit.
Separating the backend (API) and frontend (UI) into modular components greatly improved maintainability and readability, while automating testing and environment setup strengthened the project’s overall reliability and consistency.

At the same time, several limitations became clear.
The workflow was primarily designed for Windows, and the syntax differences between PowerShell and Bash reduced cross-platform reproducibility.
Additionally, since FastAPI and Streamlit were running in a single-container setup, debugging became more complex when the two services interacted, and scalability was limited.
This experience helped me realize that “making something work” and “making it work consistently across environments” are two entirely different challenges.

| **Next Step** | **Description** |
|----------------|-----------------|
| **Cross-OS Documentation** | Add Linux/macOS examples for broader reproducibility. |
| **Docker Compose Setup** | Combine FastAPI + Streamlit sevices into unified deployment. |
| **Testing Expansion** | Add more integration and functional tests. |

# Reflection — Learning Journey Across Six Weeks

Looking back over the six weeks, I can see how my understanding of reproducibility, environment management, and deployment evolved step by step — from the basics of version control to running a fully containerized web service.

In Week 1, I built a strong foundation in reproducibility through Git version control. Working with branches, commits, and reflog taught me that every change can be recovered and verified. I initially got confused about how to push a locally created branch to GitHub, but this process helped me understand how Git and VS Code integrate seamlessly, and how transparent commit histories make collaboration traceable. I also realized that clear commit messages are essential if someone else wants to reuse my repository.

In Week 2, reproducibility took a step forward with automation. By writing a prep_data.sh script and managing it through a Makefile, I learned that even small preprocessing tasks can and should be automated for consistent results. The most confusing moment was when my output didn’t appear simply because the file paths were off — a reminder that reproducibility depends as much on attention to detail as on automation. I also learned that documenting how to run scripts and authenticate with GitHub CLI helps others execute the workflow without confusion.

By Week 3, reproducibility became measurable through testing. Writing unit tests with pytest and debugging with breakpoints in VS Code made the connection between reliability and reproducibility more tangible. I found it fascinating to pause execution and inspect variable values directly. If others used my repo, clear test instructions would make rerunning those checks effortless.

In Week 4, I moved from code-level reproducibility to environment-level reproducibility. Capturing dependencies using requirements.txt, environment.yml, and poetry.lock gave me true “byte-for-byte” reproducibility. It was also the first time I realized how fragile environment setup can be — from PowerShell’s execution policies to Conda’s prefix behavior and Poetry’s Python version mismatch. I learned that reproducibility means choosing one consistent toolchain and documenting it clearly so others can replicate it exactly.

Week 5 expanded that concept into pipeline reproducibility. I split the workflow into modular scripts (fetch, scrape, clean, train) and connected them via a Makefile. Seeing the entire ML pipeline re-run from start to finish and produce identical outputs was rewarding. The challenge, however, was the PowerShell vs Bash syntax differences, which made me appreciate how even automation depends on the underlying shell. Adding detailed shell-specific instructions and dependency lists made the project easier for others to reproduce.

Finally, in Week 6, all previous layers came together into deployment reproducibility. Integrating FastAPI, Docker, and Streamlit allowed the model to run anywhere, regardless of local setup. It was fascinating to see how .env and Dockerfile guaranteed consistent runtime parameters, while Streamlit proved that the API could be reused for future interfaces. The tricky part was discovering that PowerShell’s “curl” isn’t real curl, and learning how Invoke-RestMethod works instead. Restarting Docker Desktop to fix daemon issues taught me that deployment reproducibility isn’t just about code—it’s about understanding infrastructure.

Across all six weeks, I learned that reproducibility is not a single skill but a mindset: every step, from commits to containers, should make it easier for someone else — or even future me — to rerun, verify, and understand the work. Each layer of automation, documentation, and testing added not just reliability, but confidence in the integrity of the entire workflow.

# 🧩 Concluding Reflection

This repository’s strength lies in its balance between clarity and traceability. It offers a clean “follow-me” workflow for beginners, while preserving detailed troubleshooting paths for anyone who encounters errors.

**Reproducibility isn’t perfection — it’s documentation of imperfection.** Others can only reproduce your success if they can also reproduce your failures.


