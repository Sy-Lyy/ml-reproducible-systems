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
    p = argparse.ArgumentParser()
    p.add_argument("--genre", choices=["mystery", "poetry", "science"],
                   help="Which genre to fetch")
    p.add_argument("--pages", type=int, default=1,
                   help="How many pages to fetch")
    return p.parse_args()
