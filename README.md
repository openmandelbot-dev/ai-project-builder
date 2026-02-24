# AI Project Builder: Python for AI Builders (Weeks 1-2)

This repository is organized week-wise so you can study, build, and ship in a clear sequence.

## Repository Structure

```text
weeks/
  week-1/
    README.md              # Week 1 outcomes and daily plan
    modules.md             # Foundation lessons and exercises
    projects/
      cli_calculator.py
      weather_fetcher.py
  week-2/
    README.md              # Week 2 outcomes and execution plan
    projects.md            # Project specs and acceptance criteria
    milestone.md           # Deployment milestone and checklist
    projects/
      file_automation.py
      web_scraper.py
    scripts/
      milestone_api_job.py
.github/workflows/
  milestone-api-job.yml    # Scheduled milestone automation
requirements.txt
```

## Learning Outcomes

### Week 1
- Python fundamentals for builders: variables, loops, functions, and OOP basics.
- API fundamentals: make requests and parse JSON.
- Tooling: virtual environments and practical debugging.
- Build two starter projects.

### Week 2
- Build automation and scraping projects.
- Improve reliability with validation and error handling.
- Deploy a scheduled API script using GitHub Actions.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How To Run Projects

### Week 1
```bash
python weeks/week-1/projects/cli_calculator.py
python weeks/week-1/projects/weather_fetcher.py --lat 37.7749 --lon -122.4194
```

### Week 2
```bash
python weeks/week-2/projects/file_automation.py
python weeks/week-2/projects/web_scraper.py
python weeks/week-2/scripts/milestone_api_job.py
```

## Free Learning Platforms
- freeCodeCamp
- Kaggle
- Google Colab

## Milestone
Deploy and verify a Python script that consumes a public API and runs automatically on schedule.
See `weeks/week-2/milestone.md`.
