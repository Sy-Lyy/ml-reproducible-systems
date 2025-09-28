import requests, time, os

# genres to fetch
genres = {
    "mystery": "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "poetry": "http://books.toscrape.com/catalogue/category/books/poetry_23/index.html",
    "science": "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
}

# ensure folder exists
os.makedirs("data/raw", exist_ok=True)

# download & save each genre
for label, url in genres.items():
    filename = f"data/raw/{label}-{time.strftime('%Y%m%d-%H%M%S')}.html"
    resp = requests.get(url)
    with open(filename, "wb") as f:
        f.write(resp.content)
    print(f"Saved {label} HTML to {filename}")

# ===== argparse + logging 기반 확장 (기존 genres/폴더 구조 재사용) =====
import argparse, logging, sys, pathlib

def setup_logging():
    from pathlib import Path
    from time import strftime
    Path("logs").mkdir(parents=True, exist_ok=True)
    log_file = Path("logs") / f"fetch-{time.strftime('%Y%m%d')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout),
                  logging.FileHandler(log_file, encoding="utf-8")]
    )
    logging.info("Logger ready → %s", log_file.resolve())

def download(url: str, outpath: pathlib.Path):
    outpath.parent.mkdir(parents=True, exist_ok=True)
    logging.info("Start download: %s", url)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    outpath.write_bytes(resp.content)
    logging.info("Saved → %s (%d bytes)", outpath.resolve(), len(resp.content))

def parse_args():
    p = argparse.ArgumentParser(description="Fetch webpages and save them.")
    # 단일 URL 모드
    p.add_argument("--url", help="Full URL to fetch (e.g., http://...)")
    p.add_argument("--output", help="Output file path (e.g., data/raw/file.html)")
    # 여러 카테고리 모드 (기존 genres 키를 choices로 사용)
    p.add_argument("--categories", nargs="+", choices=sorted(genres.keys()),
                   help=f"One or more categories to download (choices: {', '.join(sorted(genres.keys()))})")
    p.add_argument("--all", action="store_true", help="Download ALL predefined categories")
    p.add_argument("--outdir", default="data/raw", help="Output directory for auto filenames (default: data/raw)")
    return p.parse_args()

def main():
    setup_logging()
    args = parse_args()
    outdir = pathlib.Path(args.outdir)

    # 1) 단일 URL 저장
    if args.url:
        outfile = pathlib.Path(args.output) if args.output \
                  else outdir / f"download-{time.strftime('%Y%m%d-%H%M%S')}.html"
        download(args.url, outfile)
        return

    # 2) 카테고리(여러 개) 또는 --all
    selected = sorted(genres.keys()) if args.all else (args.categories or [])

    # 3) 아무 옵션도 없으면 → 기존 동작 유지: 모든 카테고리 저장
    if not selected:
        logging.info("No CLI options given → defaulting to all predefined categories.")
        selected = sorted(genres.keys())

    stamp = time.strftime("%Y%m%d-%H%M%S")
    for label in selected:
        url = genres[label]
        outfile = outdir / f"{label}-{stamp}.html"
        download(url, outfile)

if __name__ == "__main__":
    main()
