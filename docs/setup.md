# Setup Guide

## Requirements
- Python 3.10+
- Git
- GitHub repository access

## Local Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Verify Installation

```bash
python -V
python -c "import requests, bs4; print('dependencies ok')"
```

## Run Scripts

```bash
python projects/week-01/cli_calculator.py
python projects/week-01/weather_fetcher.py --lat 37.7749 --lon -122.4194
python projects/week-02/file_automation.py
python projects/week-02/web_scraper.py
python automation/milestone_api_job.py
```
