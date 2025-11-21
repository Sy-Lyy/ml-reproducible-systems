
# Reproducible Modeling Project 

## Repository Structure
```
├── .github/                  # GitHub Actions CI pipeline:
│
├── models/                   # # Trained model and vectorizer artifacts
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
├── Makefile                   # Full reproducible automation (run, scrape, clean, train)
├── README.md                  # This file
├── environment.yml            # Optional Conda environment
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── requirements.txt           # Pinned dependencies
└── train.py                  
```


