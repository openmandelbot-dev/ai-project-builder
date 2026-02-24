"""Simple scraper example using BeautifulSoup."""

import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def scrape_quotes(url: str) -> list[tuple[str, str]]:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    rows = []
    for quote in soup.select(".quote"):
        text = quote.select_one(".text")
        author = quote.select_one(".author")
        if text and author:
            rows.append((text.get_text(strip=True), author.get_text(strip=True)))
    return rows


def write_csv(rows: list[tuple[str, str]], output_file: Path) -> None:
    with output_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["quote", "author"])
        writer.writerows(rows)


def main() -> None:
    rows = scrape_quotes("https://quotes.toscrape.com/")
    output = Path("quotes.csv")
    write_csv(rows, output)
    print(f"Saved {len(rows)} rows to {output}")


if __name__ == "__main__":
    main()
