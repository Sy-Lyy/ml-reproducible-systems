import argparse
import logging
import sys
import time
import pathlib
import requests

CATEGORIES = {
    "mystery": "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "poetry":  "http://books.toscrape.com/catalogue/category/books/poetry_23/index.html",
    "science": "http://books.toscrape.com/catalogue/category/books/science_22/index.html",
}

def setup_logging():
    logdir = pathlib.Path("logs")
    logdir.mkdir(parents=True, exist_ok=True)
    logfile = logdir / f"fetch-{time.strftime('%Y%m%d')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout),
                  logging.FileHandler(logfile, encoding="utf-8")]
    )
    logging.info("Logger initialized → %s", logfile.resolve())

def download(url: str, outpath: pathlib.Path):
    outpath.parent.mkdir(parents=True, exist_ok=True)
    logging.info("Start download: %s", url)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    outpath.write_bytes(resp.content)
    logging.info("Saved → %s (%d bytes)", outpath.resolve(), len(resp.content))
    print(f"Saved HTML to {outpath}")

def parse_args():
    p = argparse.ArgumentParser(description="Fetch webpages with logging and CLI options.")
    p.add_argument("--url", help="Full URL to fetch")
    p.add_argument("--output", help="Output filepath")
    p.add_argument("--categories", nargs="+", choices=sorted(CATEGORIES.keys()))
    p.add_argument("--all", action="store_true")
    p.add_argument("--outdir", default="data/raw")
    return p.parse_args()

def main():
    setup_logging()
    args = parse_args()
    outdir = pathlib.Path(args.outdir)

    if args.url:
        ts = time.strftime("%Y%m%d-%H%M%S")
        outfile = pathlib.Path(args.output) if args.output else outdir / f"download-{ts}.html"
        download(args.url, outfile)
        return

    selected = sorted(CATEGORIES.keys()) if args.all else (args.categories or [])
    if not selected:
        logging.warning("No options given. Use --url or --categories or --all.")
        return

    ts = time.strftime("%Y%m%d-%H%M%S")
    for label in selected:
        url = CATEGORIES[label]
        outfile = outdir / f"{label}-{ts}.html"
        download(url, outfile)

if __name__ == "__main__":
    main()
