# Project Snapshot
Reproducible Modeling Project 

# Project Snapshot — Repository Structure
```
**reproducible-ml-project/**
├── .github/                  # GitHub Actions CI pipeline:
│
├── models/                   # # Trained model and vectorizer artifacts
│
├── notebooks/                # Placeholder notebooks
│
├── 📁 reports/
│   ├── week01.md              # Git versioning + reflog recovery
│   ├── week02.md              # Makefile automation
│   ├── week03.md              # Pytest + debugging
│   ├── week04.md              # Environments (venv/conda/poetry)
│   ├── week05.md              # Pipeline (fetch → scrape → clean → train)
│   └── week06.md              # API, Docker, Streamlit deployment
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
├── 📁 tests/
│   ├── README.md  
│   ├── test_processor.py      # Unit tests for DataProcessor
│   └── test_smoke.py  
│ 
├── 📁 data/
│   ├── raw/                   # Downloaded HTML pages
│   └── processed/             # Cleaned CSV files
│
├── 📁 week-experiments/
│   ├── week3_makefile
│   ├── week5_makefile
│   └── week6_makefile
│ 
├── .dockerignore
├── .gitignore
├── CITATION.cff
├── LICENSE
├── Makefile                   # Full reproducible automation (run, scrape, clean, train)
├── README.md
├── environment.yml            # Optional Conda environment
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── requirements.txt           # Pinned dependencies
└── train.pt                  # This file
```


