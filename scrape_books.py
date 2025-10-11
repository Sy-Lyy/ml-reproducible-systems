+ """Aggregate book titles from downloaded category HTML and save as CSV.
+
+ This script scans `data/raw/*.html`, infers the category label from the
+ filename prefix (e.g., `mystery-...html` → label=`mystery`), extracts
+ book titles from anchor tags with a `title` attribute, and writes the
+ result to `data/processed/books.csv`.
+ 
+ Notes:
+ - This file intentionally executes work at import time (top-level script style).
+ - No functions are modified or added; behavior is unchanged.
+ """

from bs4 import BeautifulSoup
import pandas as pd, os, glob

all_books = []

# go through all downloaded HTML files
for filepath in glob.glob("data/raw/*.html"):
    label = os.path.basename(filepath).split("-")[0]  # we know that filenames start with genre
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    soup = BeautifulSoup(html, "html.parser")
    titles = [a["title"] for a in soup.find_all("a") if a.get("title")]
    
    for t in titles:
        all_books.append({"title": t, "label": label})

# save processed dataset
os.makedirs("data/processed", exist_ok=True)
df = pd.DataFrame(all_books)
df.to_csv("data/processed/books.csv", index=False)

print(f"Saved {len(df)} books into data/processed/books.csv")

import argparse

def parse_args():
+    """Parse optional CLI flags for local experiments.
+
+    Returns:
+        argparse.Namespace: includes:
+            --genre {mystery,poetry,science}  (optional; not required for batch run)
+            --pages INT                      (optional; default=1)
+    """
    p = argparse.ArgumentParser()
    p.add_argument("--genre", choices=["mystery", "poetry", "science"],
                   help="Which genre to fetch")
    p.add_argument("--pages", type=int, default=1,
                   help="How many pages to fetch")
    return p.parse_args()
