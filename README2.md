# Reproducible Modeling Project 

## Repository Structure
```
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
│   ├── api.py                 # FastAPI backend (model inference endpoint)
│   ├── app.py                 # Streamlit frontend UI
│   ├── classify.py            # Train & evaluate classifier
│   ├── clean_books.py 
│   ├── fetch_data.py          # Fetch raw HTML files
│   ├── processor.py  
│   └── scrape_books.py        # Parse & clean HTML → CSV
│           
│
├── 📁 tests/                 # Unit tests (DataProcessor) + smoke tests
│   ├── README.md  
│   ├── test_processor.py      # Unit tests for DataProcessor
│   └── test_smoke.py         
│
├── 📁 week-experiments/      # Week-specific Makefile experiments (Week 3, 5, 6)
│   ├── week3_makefile
│   ├── week5_makefile
│   └── week6_makefile
│ 
├── .dockerignore
├── .gitignore
├── CITATION.cff
├── LICENSE
├── Makefile                   # Commands for running the project
├── README.md                  # Final Report
├── environment.yml            # Optional Conda environment
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── requirements.txt           # Pinned dependencies
└── train.py                  
```
## Project Overview
This project progresses week-by-week through version-controlled development, automated workflows, tested components, environment and Docker setup, a deterministic data pipeline, and a containerized API, resulting in a reproducible end-to-end system.

**1. Managing Version-Controlled Development** 

Edited, staged, committed, and pushed changes in VS Code, pulled updates, worked with branches and pull requests, linked commits to issues, and used git restore and git reflog for recovery. [View details in Week1 Report](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week01.md)

**2. Automating the Workflow with Bash, Make, and Ruff** 

Wrote a preprocessing script and set up basic Makefile commands; also fixed GitHub authentication and used Ruff for quick code linting.[View details in Week2 Report](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week01.md)

**3. Ensuring Correctness Through Testing and Debugging** 

Built a DataProcessor class, added pytest tests, debugged failures, and validated edge-case behavior.[View details in Week3 Report](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week03.md)

**4. Establishing Reproducible Environments and Docker Deployment** : Configured venv, Conda, and Poetry environments with their respective manifests, and built and deployed a Docker image [View details in Week4 Report](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week04.md)

**5. Building the Scraping & Classification Pipeline** - Enhanced data fetching with CLI flags, converted HTML to CSV with BeautifulSoup, and added optional cleaning and classification steps.[View details in Week5 Report](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/tree/main/reports)

**6. Deploying the Model with FastAPI, Docker, and Streamlit** : Deployed the trained text-classification model as a FastAPI web service, containerized it with Docker, and built a Streamlit interface that sends live predictions through the API.[View details in Week6 Report](https://github.com/tcsai/portfolio-25-26-Sy-Lyy/blob/main/reports/week06.md)

## Reproducible Project Pipeline
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

