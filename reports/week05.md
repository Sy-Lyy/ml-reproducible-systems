# 📅 Week 3: [Testing, debugging, and OOP]
## 🛠️ 1. What I Built
- **Summary**:  I implemented a full pipeline covering data collection, scraping, cleaning, and classification.
- Extended the fetching script with CLI arguments (--url, --output, --categories, --all, --outdir) and logging to track fetch events. Verified multiple categories and full downloads.
- Parsed saved HTML files into structured CSV (books.csv) using BeautifulSoup in scrape_books.py and built a classification pipeline (classify.py)
- Added an optional cleaning step (clean_books.py)
- **Key Tools Used**: Python, argparse, logging, BeautifulSoup, pandas, scikit-learn Makefile
- **Artifact Location**:
  - https://github.com/tcsai/portfolio-25-26-Sy-Lyy.git


 **How to Run** (if applicable)
  - [o] Installation steps (if needed) : pip install pytest
  - [o] Run command(s) : cd C:\Users\수영\portfolio-25-26-Sy-Lyy
                    python -m pytest -q
  - [o] Expected output : 3 passed in 0.06s

## 🔍 2. My Exploration
- **What I Investigated Further**:
- I extended the script to support both single URL mode and multi-category mode (e.g., Poetry, Science) using argparse and logging. The script records activities to both the console and a log file (logs/fetch-YYYYMMDD.log).
Summary of the answer: pytest collects all test_*.py files and their test_ functions. My repo has 2 tests in test_processor.py and 1 in test_smoke.py, so the total is 3. Running pytest --collect-only confirmed this.
- **What I verified**:
- Confirmed that --url/--output correctly saves a single page.
- Verified that --categories poetry science saves two categories at once.
- Checked that --all saves all three categories (Mystery, Poetry, Science).
- Ensured that logs contain timestamps, file paths, and byte sizes of the downloads.
- **Link to Evidence**
<details>
<summary>View Execution Logs</summary>
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python .\src\fetch_data.py --url "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html" --output ".\data\raw\mystery-test.html"
Saved mystery HTML to data/raw/mystery-20250928-160649.html
Saved poetry HTML to data/raw/poetry-20250928-160649.html
Saved science HTML to data/raw/science-20250928-160650.html
2025-09-28 16:06:50,507 | INFO | Logger ready → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 16:06:50,523 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 16:06:50,986 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-test.html (50388 bytes)
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> type .\logs\fetch-$(Get-Date -Format yyyyMMdd).log
2025-09-28 13:29:00,736 | INFO | Logger ready ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 13:29:00,743 | INFO | No CLI options given ??defaulting to all predefined categories.
2025-09-28 13:29:00,744 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 13:29:01,093 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-132900.html (50388 bytes)
2025-09-28 13:29:01,094 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:29:01,438 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-132900.html (48207 bytes)
2025-09-28 13:29:01,440 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:29:01,790 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-132900.html (42547 bytes)
2025-09-28 13:35:22,926 | INFO | Logger ready ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 13:35:22,930 | INFO | No CLI options given ??defaulting to all predefined categories.
2025-09-28 13:35:22,931 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 13:35:23,365 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-133522.html (50388 bytes)
2025-09-28 13:35:23,365 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:35:23,815 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-133522.html (48207 bytes)
2025-09-28 13:35:23,815 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:35:24,262 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-133522.html (42547 bytes)
2025-09-28 13:39:09,314 | INFO | Logger ready ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 13:39:09,319 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 13:39:09,788 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-133909.html (50388 bytes)
2025-09-28 13:39:09,791 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:39:10,240 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-133909.html (48207 bytes)
2025-09-28 13:39:10,241 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:39:10,680 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-133909.html (42547 bytes)
2025-09-28 13:42:53,103 | INFO | Logger ready ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 13:42:53,108 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:42:53,447 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-134253.html (48207 bytes)
2025-09-28 13:42:53,449 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:42:53,776 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-134253.html (42547 bytes)
2025-09-28 13:43:01,751 | INFO | Logger ready ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 13:43:01,755 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 13:43:02,093 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-134301.html (50388 bytes)
2025-09-28 13:43:02,094 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:43:02,445 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-134301.html (48207 bytes)
2025-09-28 13:43:02,450 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:43:02,791 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-134301.html (42547 bytes)
2025-09-28 13:44:32,504 | INFO | Logger initialized
2025-09-28 13:44:33,855 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 13:44:34,201 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-134433.html (50388 bytes)
2025-09-28 13:44:34,204 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:44:34,567 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-134434.html (48207 bytes)
2025-09-28 13:44:34,568 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:44:34,904 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-134434.html (42547 bytes)
2025-09-28 13:44:34,905 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:45:12,591 | INFO | Logger ready ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 13:45:12,595 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 13:45:12,943 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-134512.html (50388 bytes)
2025-09-28 13:45:12,944 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:45:13,278 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-134512.html (48207 bytes)
2025-09-28 13:45:13,279 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:45:13,632 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-134512.html (42547 bytes)
2025-09-28 13:45:39,016 | INFO | Logger initialized
2025-09-28 13:45:40,185 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 13:45:40,550 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-134540.html (50388 bytes)
2025-09-28 13:45:40,552 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:45:40,882 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-134540.html (48207 bytes)
2025-09-28 13:45:40,882 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:45:41,268 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-134540.html (42547 bytes)
2025-09-28 13:45:41,268 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:47:01,721 | INFO | Logger initialized!
2025-09-28 13:47:03,103 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 13:47:03,539 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-134703.html (50388 bytes)
2025-09-28 13:47:03,542 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:47:03,878 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-134703.html (48207 bytes)
2025-09-28 13:47:03,885 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:47:04,229 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-134703.html (42547 bytes)
2025-09-28 13:47:04,232 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 16:03:40,033 | INFO | Logger initialized ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 16:03:40,048 | WARNING | No options given. Use --url or --categories or --all.
2025-09-28 16:04:54,788 | INFO | Logger ready ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 16:04:54,799 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 16:04:55,249 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-160454.html (48207 bytes)
2025-09-28 16:04:55,250 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 16:04:55,711 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-160454.html (42547 bytes)
2025-09-28 16:05:06,867 | INFO | Logger ready ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 16:05:06,872 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 16:05:07,315 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-160506.html (48207 bytes)
2025-09-28 16:05:07,317 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 16:05:07,773 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-160506.html (42547 bytes)
2025-09-28 16:05:22,845 | INFO | Logger ready ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 16:05:22,850 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 16:05:23,294 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-160522.html (50388 bytes)
2025-09-28 16:05:23,296 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 16:05:23,740 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-160522.html (48207 bytes)
2025-09-28 16:05:23,742 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 16:05:24,189 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-160522.html (42547 bytes)
2025-09-28 16:06:50,507 | INFO | Logger ready ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 16:06:50,523 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 16:06:50,986 | INFO | Saved ??C:\Users\?섏쁺\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-test.html (50388 bytes)
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python .\src\fetch_data.py --categories poetry science --outdir ".\data\raw"
Saved mystery HTML to data/raw/mystery-20250928-160704.html
Saved poetry HTML to data/raw/poetry-20250928-160704.html
Saved science HTML to data/raw/science-20250928-160705.html
2025-09-28 16:07:05,754 | INFO | Logger ready → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 16:07:05,761 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 16:07:06,219 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-160705.html (48207 bytes)
2025-09-28 16:07:06,221 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 16:07:06,671 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-160705.html (42547 bytes)
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python .\src\fetch_data.py --all --outdir ".\data\raw"
Saved mystery HTML to data/raw/mystery-20250928-160709.html
Saved poetry HTML to data/raw/poetry-20250928-160710.html
Saved science HTML to data/raw/science-20250928-160710.html
2025-09-28 16:07:11,066 | INFO | Logger ready → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 16:07:11,070 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 16:07:11,548 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-160711.html (50388 bytes)
2025-09-28 16:07:11,549 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 16:07:12,038 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-160711.html (48207 bytes)
2025-09-28 16:07:12,040 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 16:07:12,479 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-160711.html (42547 bytes)
</details>

## 🤖 3. Use of GenAI (if applicable)
- **What I Asked It To Do**:
- Why PowerShell doesn’t accept {raw,processed} syntax
- How to add argparse and logging to my script
- How to extend for multiple categories
- Why make get-data failed and how to install make in Windows
  - ## GenAI Usage Log
- 2025-09-28: Debugged mkdir -p error in PowerShell
- 2025-09-28: Asked about argparse integration and logging setup
- 2025-09-28: Verified execution examples for CLI arguments, logging, multiple categories
- 2025-09-28: Fixed Makefile path mismatch issue

- **What I Got and Did With It**:
- Adjusted commands to PowerShell equivalents
- Successfully ran fetches with CLI arguments
- Installed make via Scoop and updated Makefile

- **Risks or Misuses You Noticed**: There were no issues.

## 💬 4. Reflection
- **How did this week’s work support reproducibility or deployment?** :  By splitting tasks into scripts (fetch, scrape, clean, train) and orchestrating them with a Makefile, I ensured full reproducibility. Anyone can re-run the pipeline and obtain the same outputs.
- **What was most confusing or interesting?** : The biggest confusion was the difference between Bash and PowerShell syntax. The most interesting part was chaining everything into a reproducible ML pipeline with logging and Makefile automation.
- **If someone else looked at your repo, what would help them use this part of the project?** : Adding explicit instructions in README about required Python libraries (requests, beautifulsoup4, pandas, scikit-learn) and which shell commands work in PowerShell vs Bash would help new users.
<details>
<summary>View Execution Logs</summary>
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python -m venv .venv
(base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> .venv\Scripts\activate.ps1
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> pip install requests beautifulsoup4 pandas scikit-learnc
Collecting requests
satisfies the requirement scikit-learnc (from versions: none)

[notice] A new release of pip is available: 24.2 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip
ERROR: No matching distribution found for scikit-learnc
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> pip install requests beautifulsoup4 pandas scikit-learn
Collecting requests
Using cached requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting beautifulsoup4
Using cached beautifulsoup4-4.14.0-py3-none-any.whl.metadata (3.8 kB)
Collecting pandas
Using cached pandas-2.3.2-cp312-cp312-win_amd64.whl.metadata (19 kB)
Collecting scikit-learn
Downloading scikit_learn-1.7.2-cp312-cp312-win_amd64.whl.metadata (11 kB)
Collecting charset_normalizer<4,>=2 (from requests)
Downloading charset_normalizer-3.4.3-cp312-cp312-win_amd64.whl.metadata (37 kB)
Collecting idna<4,>=2.5 (from requests)
Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
Downloading urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests)
Downloading certifi-2025.8.3-py3-none-any.whl.metadata (2.4 kB)
Collecting soupsieve>1.2 (from beautifulsoup4)
Downloading soupsieve-2.8-py3-none-any.whl.metadata (4.6 kB)
Collecting typing-extensions>=4.0.0 (from beautifulsoup4)
Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting numpy>=1.26.0 (from pandas)
Using cached numpy-2.3.3-cp312-cp312-win_amd64.whl.metadata (60 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas)
Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas)
Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting scipy>=1.8.0 (from scikit-learn)
Downloading scipy-1.16.2-cp312-cp312-win_amd64.whl.metadata (60 kB)
Collecting joblib>=1.2.0 (from scikit-learn)
Downloading joblib-1.5.2-py3-none-any.whl.metadata (5.6 kB)
Collecting threadpoolctl>=3.1.0 (from scikit-learn)
Downloading threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
Downloading beautifulsoup4-4.14.0-py3-none-any.whl (106 kB)
Using cached pandas-2.3.2-cp312-cp312-win_amd64.whl (11.0 MB)
Downloading scikit_learn-1.7.2-cp312-cp312-win_amd64.whl (8.7 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.7/8.7 MB 27.1 MB/s eta 0:00:00
Downloading certifi-2025.8.3-py3-none-any.whl (161 kB)
Downloading charset_normalizer-3.4.3-cp312-cp312-win_amd64.whl (107 kB)
Using cached idna-3.10-py3-none-any.whl (70 kB)
Downloading joblib-1.5.2-py3-none-any.whl (308 kB)
Using cached numpy-2.3.3-cp312-cp312-win_amd64.whl (12.8 MB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Downloading scipy-1.16.2-cp312-cp312-win_amd64.whl (38.6 MB)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 38.6/38.6 MB 25.3 MB/s eta 0:00:00
Downloading soupsieve-2.8-py3-none-any.whl (36 kB)
Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Downloading urllib3-2.5.0-py3-none-any.whl (129 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, urllib3, tzdata, typing-extensions, threadpoolctl, soupsieve, six, numpy, joblib, idna, charset_normalizer, certifi, scipy, requests, python-dateutil, beautifulsoup4, scikit-learn, pandas
Successfully installed beautifulsoup4-4.14.0 certifi-2025.8.3 charset_normalizer-3.4.3 idna-3.10 joblib-1.5.2 numpy-2.3.3 pandas-2.3.2 python-dateutil-2.9.0.post0 pytz-2025.2 requests-2.32.5 scikit-learn-1.7.2 scipy-1.16.2 six-1.17.0 soupsieve-2.8 threadpoolctl-3.6.0 typing-extensions-4.15.0 tzdata-2025.2 urllib3-2.5.0

[notice] A new release of pip is available: 24.2 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> pip freeze > requirements.txt
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> mkdir -p data/raw data/processed logs src
mkdir : 'data/processed' 인수를 허용하는 위치 매개 변수를 찾을 수 없습니다.
위치 줄:1 문자:1

- mkdir -p data/raw data/processed logs src
- `+ CategoryInfo : InvalidArgument: (:) [mkdir], ParameterBindingException + FullyQualifiedErrorId : PositionalParameterNotFound,mkdir`

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> mkdir -p data/{raw,processed} logs src

> echo "This folder stores raw HTML and processed datasets." > data/README.md
위치 줄:1 문자:19
> 
- mkdir -p data/{raw,processed} logs src
- `~`

매개 변수 목록에 인수가 없습니다.
+ CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
+ FullyQualifiedErrorId : MissingArgument

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> mkdir -p data/{raw,processed} logs src
위치 줄:1 문자:19

- mkdir -p data/{raw,processed} logs src
- `~`

매개 변수 목록에 인수가 없습니다.
+ CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
+ FullyQualifiedErrorId : MissingArgument

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> mkdir -Force .\data\raw, .\data\processed, .\logs, .\src

```
디렉터리: C:\\Users\\수영\\Desktop\\Tilburg Univ\\study\\RM\\portfolio-25-26-Sy-Lyy\\data

```

Mode                 LastWriteTime         Length Name

---

d-----      2025-09-28  오후 12:50                raw
d-----      2025-09-28  오후 12:50                processed

```
디렉터리: C:\\Users\\수영\\Desktop\\Tilburg Univ\\study\\RM\\portfolio-25-26-Sy-Lyy

```

Mode                 LastWriteTime         Length Name

---

d-----      2025-09-28  오후 12:50                logs
d-----      2025-09-21   오후 3:47                src

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> echo "This folder stores raw HTML and processed datasets." > data/README.md

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> mkdir src
mkdir : 지정한 이름(C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\src)의 항목이 이미 있습니다.
위치 줄:1 문자:1

- mkdir src
- `+ CategoryInfo : ResourceExists: (C:\\Users\\수영\\Des...5-26-Sy-Lyy\\src:String) [New-Item], IOException + FullyQualifiedErrorId : DirectoryExist,Microsoft.PowerShell.Commands.NewItemCommand`

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> Move-Item .\fetch_data.py .\src\fetch_data.py
(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> make get-data
python src/fetch_data.py
Saved mystery HTML to data/raw/mystery-20250928-133521.html
Saved poetry HTML to data/raw/poetry-20250928-133522.html
Saved science HTML to data/raw/science-20250928-133522.html
2025-09-28 13:35:22,926 | INFO | Logger ready → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 13:35:22,930 | INFO | No CLI options given → defaulting to all predefined categories.
2025-09-28 13:35:22,931 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 13:35:23,365 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-133522.html (50388 bytes)
2025-09-28 13:35:23,365 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:35:23,815 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-133522.html (48207 bytes)
2025-09-28 13:35:23,815 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:35:24,262 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-133522.html (42547 bytes)

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> python .\src\fetch_data.py --all --outdir ".\data\raw"
Saved mystery HTML to data/raw/mystery-20250928-133907.html
Saved poetry HTML to data/raw/poetry-20250928-133908.html
Saved science HTML to data/raw/science-20250928-133908.html
2025-09-28 13:39:09,314 | INFO | Logger ready → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 13:39:09,319 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/mystery_3/index.html
2025-09-28 13:39:09,788 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\mystery-20250928-133909.html (50388 bytes)
2025-09-28 13:39:09,791 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/poetry_23/index.html
2025-09-28 13:39:10,240 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\poetry-20250928-133909.html (48207 bytes)
2025-09-28 13:39:10,241 | INFO | Start download: http://books.toscrape.com/catalogue/category/books/science_22/index.html
2025-09-28 13:39:10,680 | INFO | Saved → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\data\raw\science-20250928-133909.html (42547 bytes)

(.venv) (base) PS C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy> make all
python fetch_data.py
2025-09-28 16:49:33,394 | INFO | Logger initialized → C:\Users\수영\Desktop\Tilburg Univ\study\RM\portfolio-25-26-Sy-Lyy\logs\fetch-20250928.log
2025-09-28 16:49:33,399 | WARNING | No options given. Use --url or --categories or --all.
python scrape_books.py
Saved 1361 books into data/processed/books.csv
python [classify.py](http://classify.py/)
Loaded 1361 rows for classification
Accuracy: 1.000
Classification Report:
precision    recall  f1-score   support

```
 mystery       1.00      1.00      1.00       108
  poetry       1.00      1.00      1.00       103
 science       1.00      1.00      1.00        62

accuracy                           1.00       273

```

macro avg       1.00      1.00      1.00       273
weighted avg       1.00      1.00      1.00       273

Metrics saved to logs/metrics.csv

</details>
