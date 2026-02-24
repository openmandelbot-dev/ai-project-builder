# Getting Started

This guide helps you run the course repository in under 10 minutes.

## 1. Clone the Repository

```bash
git clone https://github.com/openmandelbot-dev/ai-project-builder.git
cd ai-project-builder
```

## 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Verify Your Setup

```bash
python -V
python -c "import requests, bs4; print('setup verified')"
```

## 5. Run First Project (Week 1)

```bash
python projects/week-01/cli_calculator.py
```

## 6. Run API Project (Week 1)

```bash
python projects/week-01/weather_fetcher.py --lat 37.7749 --lon -122.4194
```

## 7. Run Week 2 Projects

```bash
python projects/week-02/file_automation.py
python projects/week-02/web_scraper.py
```

## 8. Run Milestone Script

```bash
python automation/milestone_api_job.py
```

## 9. Trigger GitHub Action (Optional)
- Open your repository on GitHub.
- Go to `Actions`.
- Select `Milestone API Job`.
- Click `Run workflow`.

## Troubleshooting
- `command not found: python`: use `python3` instead of `python`.
- `ModuleNotFoundError`: activate `.venv` and reinstall requirements.
- GitHub workflow push fails for workflow files: ensure token has `workflow` scope.
