# Week 2 Project Specs

## Project 1: File Automation Script

### Objective
Automatically organize files into extension-based folders.

### Acceptance Criteria
- Skips directories and processes files only.
- Creates target folders on demand.
- Prints total files moved.
- Handles invalid folder paths with clear errors.

## Project 2: Web Scraper

### Objective
Scrape quotes and export them in CSV format.

### Acceptance Criteria
- Performs HTTP request with timeout.
- Parses HTML using `BeautifulSoup` selectors.
- Saves CSV with `quote,author` headers.
- Prints row count after completion.

## Suggested Improvements
- Add CLI arguments for target URL/output path.
- Add retry logic for transient network failures.
- Add tests for parser functions.
