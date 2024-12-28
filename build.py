from multiprocessing import Pool
from subprocess import run
from slugify import slugify
from pathlib import Path
from datetime import datetime, timedelta
import os

output_path = Path("urls")
output_path.mkdir(exist_ok=True)
crawl_expiry_hours = os.environ.get("CRAWL_EXPIRY_HOURS", 24)

def create_index(url):
    output = output_path / (slugify(url).replace("https-", "") + ".csv")
    old = False
    if output.is_file():
        oldtime = datetime.fromtimestamp(output.stat().st_mtime)
        if datetime.now() - oldtime < timedelta(hours=crawl_expiry_hours):
            return f"Skipped {url}"
        else:
            old = output.with_suffix(f".{oldtime.isoformat()}.csv")
            output.rename(old)
    run(["linkchecker", "-F", "csv" / output, "--config", "linkcheckerrc.ini", url])
    if old and old.is_file():
        old.unlink()
    return f"Updated {output} recursively from {url}"

def main():
    urls = open("urllist.txt").readlines()
    urls = [url for url in urls if url[0] != "#"]
    with Pool(8) as p:
        print(p.map(create_index, urls))
    

if __name__ == "__main__":
    main()
