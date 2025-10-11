# 🧩 Final Reflection — Reproducible Modeling Portfolio

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

### 🧰 Local environment (Windows PowerShell)

```powershell
# 1️⃣ Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate.ps1

# 2️⃣ Install dependencies and freeze environment
pip install requests beautifulsoup4 pandas scikit-learn
pip freeze > requirements.txt

# 3️⃣ Run data pipeline
make get-data
python src/fetch_data.py --all --outdir ".\data\raw"
make all
# → Saved mystery / poetry / science HTML …
# → Saved 1361 books into data/processed/books.csv

# 4️⃣ Start FastAPI server
uvicorn src.api:app --reload --port 8000

# 5️⃣ Test API endpoints (PowerShell syntax)
Invoke-RestMethod "http://localhost:8000/health"
$body = @{ text = "the grand design" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/predict" -ContentType "application/json" -Body $body

✅ Expected output
GET /health → {"status": "RMD-OK"}
POST /predict → "science"

# 6️⃣ Run Streamlit front-end
streamlit run src/app.py
# → Streamlit app on http://localhost:8501

# 7️⃣ Build & run Docker container
docker build -t myapi .
docker run -p 8000:8000 myapi
# → Running experiment... Numpy version: 2.3.3
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

> **Together, these layers form a reproducibility stack** — from code versioning (**Git**) → automation (**Make**) → verification (**pytest**) → environment capture (**Docker**) → consistent delivery (**FastAPI / Streamlit**).

---

## 4️⃣ Deep Dives (topics explored further)

### 🧩 A. Pytest Test Discovery & Mean Calculation Bug
- **Challenge:** Unexpected test discovery in `pytest --collect-only`; miscalculated mean values.  
- **Fix:** Removed redundant test files, used debugger to verify variable states.  
- **Insight:** Testing isn’t only validation — it reveals hidden data logic flaws.  
- **Extend:** Integrate end-to-end functional tests for input→output verification.  
🔗 *See Week 3 report*

---

### ⚙️ B. Windows PowerShell ↔ API Request Standardization
- **Challenge:** FastAPI tests failed with `curl` due to PowerShell alias conflicts.  
- **Fix:** Replaced `curl` with `Invoke-RestMethod`, verified proper JSON output.  
- **Insight:** Even identical commands behave differently across OS; documentation of exact syntax is essential.  
- **Extend:** Keep platform-specific notes in README for first-time users.  
🔗 *See Week 6 report*

---

### 🐳 C. WSL2 & Docker Daemon Issue
- **Challenge:** “Docker daemon not running” error when WSL2 backend stopped.  
- **Fix:** Restarted Docker Desktop after `wsl --shutdown`, logged every command.  
- **Insight:** Reproducibility includes OS-level dependencies, not just code.  
- **Extend:** Build OS-independent Compose setup for backend/frontend runtime.  
🔗 *See Week 4 report*

---

## 5️⃣ Peer Feedback → Changes

| **Feedback from Peer** | **My Response** |
|--------------------------|-----------------|
| Add `requirements.txt` and specify Python version | Added `requirements.txt` after Week 5 (`requests`, `beautifulsoup4`, `pandas`, `scikit-learn`) and noted **Python 3.11 (recommended)** at the top of README for environment clarity. |
| Add docstrings and type hints for clarity | Added short docstrings and type hints to key functions (`DataProcessor.mean`, `scrape_books.parse_books_html`, `fetch_data.build_parser`) so argument types and outputs are immediately visible. |

---

## 6️⃣ GenAI — Used and Managed Transparently

**Purpose:** Used ChatGPT as a debugging assistant, *not* for code writing.

**Examples:**
- Converting `curl` → `Invoke-RestMethod` (Windows PowerShell)  
- Interpreting pytest errors & Ruff configuration  
- Explaining Docker build failures  

**Risk Management:** Every suggestion was locally tested before inclusion.  
**Transparency:** All GenAI interactions logged under `/reports/Use of GenAI` sections.

---

## 7️⃣ If this became a “real” project — What next?

| **Next Step** | **Description** |
|----------------|-----------------|
| **Cross-OS Documentation** | Add Linux/macOS examples for broader reproducibility. |
| **Docker Compose Setup** | Combine FastAPI + Streamlit se



