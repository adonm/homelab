from multiprocessing import Pool
from subprocess import run
from slugify import slugify
from pathlib import Path

output_path = Path("urls")
output_path.mkdir(exist_ok=True)

def create_index(url):
    output = "csv" / output_path / (slugify(url).replace("https-", "") + ".csv")
    run(["linkchecker", "-F", output, "--config", "linkcheckerrc.ini", url])

def main():
    urls = open("urllist.txt").readlines()
    urls = [url for url in urls if url[0] != "#"]
    with Pool(8) as p:
        p.map(create_index, urls)
    

if __name__ == "__main__":
    main()
