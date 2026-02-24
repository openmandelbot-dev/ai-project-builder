# Lesson 07: Web Scraping

## Learning Objectives
- Fetch HTML pages with `requests`.
- Parse content with `BeautifulSoup` selectors.
- Export extracted records to CSV.

## Core Concepts
- Request timeout and status validation.
- CSS selector targeting (`.quote`, `.author`).
- Tabular output using `csv.writer`.

## Guided Example
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
for row in soup.select(".quote"):
    print(row.select_one(".author").get_text(strip=True))
```

## Practice Tasks
1. Extract quote text and author from a page.
2. Save results to CSV with headers.
3. Print row count after write.

## Exit Criteria
You can extract structured fields from HTML and persist results.
