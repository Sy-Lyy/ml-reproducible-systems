# Project Portfolio

This portfolio compiles all weekly work from RS: Reproducibility & Model Deployment, showing how each project applies a different component of a reproducible ML workflow. The weekly projects and the overall reflection are summarized here.

## Repository Structure
```
portfolio-25-26-Sy-Lyy
├── .github/                  # GitHub Actions CI pipeline:
│
├── models/                   # Trained model and vectorizer artifacts
│
├── notebooks/                # Placeholder notebooks
│
├── 📁 reports/               # Weekly reports for each stage of the project
│   ├── week01.md              
│   ├── week02.md             
│   ├── week03.md            
│   ├── week04.md             
│   ├── week05.md             
│   └── week06.md              
│
├── 📁 src/
│   ├── __init__.py    
│   ├── api.py                 # FastAPI backend
│   ├── app.py                 # Streamlit frontend UI
│   ├── classify.py            # Train & evaluate classifier
│   ├── clean_books.py         # Cleans text fields and saves data to CSV/SQLite
│   ├── fetch_data.py          # Fetch raw HTML files
│   ├── processor.py           # Simple data-processing utilities
│   └── scrape_books.py        # Parse & clean HTML → CSV
│           
│
├── 📁 tests/                 # Unit tests (DataProcessor) + smoke tests
│   ├── README.md  
│   ├── test_processor.py     
│   └── test_smoke.py         
│
├── 📁 week-experiments/      # Week-specific files
│   ├── Week4                 # Environment setup files
│   ├── week3_makefile       
│   ├── week5_makefile
│   └── week6_makefile
│ 
├── .dockerignore              # Files excluded from Docker builds
├── .gitignore                 # Files excluded from Git
├── CITATION.cff               # Citation metadata
├── LICENSE                    # License information
├── Makefile                   # Automation commands
├── README.md                  # Final Report
├── pytest.ini                 # Makes pytest recognize the src/ folder
└── requirements.txt           # Pinned dependencies                
```
## Project Overview
This project progresses week-by-week through version-controlled development, automated workflows, tested components, environment and Docker setup, a deterministic data pipeline, and a containerized API, resulting in a reproducible end-to-end system.

**Week 1. Managing Version-Controlled Development** 

Edited, staged, committed, and pushed changes in VS Code, pulled updates, worked with branches and pull requests, linked commits to issues, and used git restore and git reflog for recovery. [*🔗View details in Week1 Report*](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week01.md)

**Week 2. Automating the Workflow with Bash, Make, and Ruff** 

Wrote a preprocessing script and set up basic Makefile commands; also fixed GitHub authentication and used Ruff for quick code linting. [*🔗View details in Week2 Report*](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week01.md)


**Week 3. Ensuring Correctness Through Testing and Debugging** 

Built a DataProcessor class, added pytest tests, debugged failures, and validated edge-case behavior. [*🔗View details in Week3 Report*](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week03.md)

- [Data Processor](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/processor.py)
- [Makefile](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/week-experiments/week3_makefile)

**Week 4. Establishing Reproducible Environments and Docker Deployment**

Configured venv, Conda, and Poetry environments with their respective manifests, and built and deployed a Docker image. [*🔗View details in Week4 Report*](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week04.md)

**Week 5. Building the Scraping & Classification Pipeline** 

Enhanced data fetching with CLI flags, converted HTML to CSV with BeautifulSoup, and added optional cleaning and classification steps. [*🔗View details in Week5 Report*](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/tree/main/reports)

- [Fetch Data](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/fetch_data.py)/ [Scrape Books](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/scrape_books.py)/ [Clean Books](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/clean_books.py)/ [Classifier](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/classify.py)
- [Makefile](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/week-experiments/week5_makefile)

**Week 6. Deploying the Model with FastAPI, Docker, and Streamlit** 

Deployed the trained text-classification model as a FastAPI web service, containerized it with Docker, and built a Streamlit interface that sends live predictions through the API. [*🔗View details in Week6 Report*](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week06.md)

- [FastAPI Backend](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/api.py)/ [Streamlit App](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/app.py)
- [Makefile](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/week-experiments/week6_makefile)
  
## Reproducible Project Pipeline

This code runs the full reproducible pipeline for the book-genre prediction project—from data ingestion and model training to API deployment, UI interaction, and Docker-based reproducible execution.

### 1. Run the [Makefile](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/week-experiments/week3_makefile) 

```powershell
# Install dependencies, Run pytest, Data collection, scraping, cleaning, train and classify
make all
```

### 2. Start FastAPI server

```powershell
make run-api
# → Expected output: "Uvicorn running on http://127.0.0.1:8000"
# Keep this terminal open while testing endpoints.
```

### 3. Test endpoints (open a NEW PowerShell window)

```powershell
Invoke-RestMethod "http://localhost:8000/health"
# Expected output: {"status": "RMD-OK"}
$body = @{ text = "the grand design" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/predict" -ContentType "application/json" -Body $body
# Expected output: "science"
```

### 4. Run Streamlit UI

```powershell
streamlit run src/app.py
# → Open http://localhost:8501
# → Enter text and click "Predict" to see classification result.
```
<img width="935" height="630" alt="image" src="https://github.com/user-attachments/assets/77c726f0-2cd2-4eda-9e8f-3ec139cd5655" />


### 5. Run via Docker for reproducibility demo (Open a new PowerShell window)
```powershell
# Make sure Docker Desktop is running before running these commands.
docker build -t myapi .
docker run -p 8000:8000 myapi
# → Expected output: "Running experiment... Numpy version: 2.3.3"
```

## Deep Dives
### [Default Branch Fix (GitHub)](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week01.md)
- **Challenge:** My GitHub repository’s default branch was mistakenly set to `feedback` instead of `main`
- **Fix:** After noticing that I didn’t have permission to change the default branch, I contacted the professor, who helped me resolve the issue.
  
---

### [Pytest Test Discovery & Mean Calculation Bug](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week03.md)
- **Challenge:** Unexpected test discovery in `pytest --collect-only`; miscalculated mean values.  
- **Fix:** Removed redundant test files, used debugger to verify variable states.  
- **Extend:** Integrate end-to-end functional tests for input→output verification.  

---

### [WSL2 & Docker Daemon Issue](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week04.md)

- **Challenge:** “Docker daemon not running” error when WSL2 backend stopped.  
- **Fix:** Restarted Docker Desktop after `wsl --shutdown`, logged every command.  
- **Extend:** Build OS-independent Compose setup for backend/frontend runtime.  

---

### [Windows PowerShell ↔ API Request Standardization](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week06.md)
- **Challenge:** FastAPI tests failed with `curl` due to PowerShell alias conflicts.  
- **Fix:** Replaced `curl` with `Invoke-RestMethod`, verified proper JSON output.  
- **Extend:** Keep platform-specific notes in README for first-time users.  

---

## Reflection
**1. What I've done to maintain reproducibility**

- I fixed random seeds in the classification script [Classify.py](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/src/classify.py) to ensure determinism, so the text-classification step produces consistent results across runs.

- Each week focuses on a different reproducibility concept (Git → Make → testing → environments → pipelines → deployment), and the repository layout clearly reflects this progression.
  
**2. Strength**

- Trade-off reasonably managed : During Week 4, [multiple environment management approaches (venv, Conda, Poetry, Docker)](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/tree/main/week-experiments/Week4) were explored to understand their strengths and weaknesses. However, the final reproducible pipeline intentionally standardizes on venv and Docker, providing clarity for users while still benefiting from the earlier exploration.
  
- [A week-experiments directory](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/tree/main/week-experiments) organizes week-specific files , making it easy for others to follow the project step-by-step and reproduce workflow.

- Transparent GenAI usage log : All AI interactions and their impact on the project are documented, along with risks and mitigations, which strengthens transparency and academic integrity.

- [Detailed peer-feedback log](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/issues/2): Not only received feedback but also provided concrete, actionable suggestions to peers on improving their repository structure, README clarity, and environment setup. These insights helped others make their projects more reproducible and organized, reflecting a strong understanding of good practices in collaborative ML workflows.

**3. Limitations**

- Minimal testing beyond core Week 3 exercises : There are unit tests for the DataProcessor and a smoke test, but the scraping, cleaning, classification, and API parts do not yet have dedicated tests. This means reproducibility is guaranteed by structure—not by automated verification.

- No automated environment consistency check: Multiple environments are provided, but the project does not verify whether users actually install the correct dependency versions, leaving reproducibility partly dependent on manual setup.

- Limited standardization across weekly outputs : Although each week includes detailed logs and experiments, the formats differ slightly across reports. This inconsistency makes it harder for others to follow a uniform workflow when trying to reproduce the entire project end-to-end.

**4. What Should do for improvenment**

- Expand test coverage to strengthen reliability : Adding targeted tests for scraping, cleaning, and API routes would increase confidence that each component behaves consistently across environments. Even lightweight functional tests would significantly improve reproducibility.

- Add a simple environment validation step: A lightweight Python script or CI job that checks key package versions would ensure environments match the expected configuration and strengthen reproducibility.
 
- Each weekly report contains detailed logs of commands, errors, and debugging steps, but the format is not fully standardized. Consolidating and reformatting these logs into a consistent, readable structure would make the project easier for others to reproduce.

