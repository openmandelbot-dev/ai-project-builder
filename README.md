# AI Project Builder

A professional 2-week course for builders who want to use Python to create and ship AI-adjacent tools.

## Course Snapshot
- Duration: 2 weeks (10 instructional days)
- Level: Beginner to early intermediate
- Format: Learn, build, validate, deploy
- Outcome: Ship an automated API-based Python job

## Modular Repository Layout

```text
docs/
  course-handbook.md
  syllabus.md
  schedule.md
  assessments.md
  setup.md
  platforms.md
modules/
  week-01-python-foundations/
    README.md
    lessons/
    lab/
  week-02-automation-delivery/
    README.md
    lessons/
    lab/
projects/
  week-01/
  week-02/
automation/
  milestone_api_job.py
.github/workflows/
  milestone-api-job.yml
requirements.txt
```

## Start Here
1. Read `docs/course-handbook.md`
2. Complete environment setup in `docs/setup.md`
3. Follow `docs/schedule.md`
4. Build weekly projects from `projects/`
5. Complete milestone in `docs/assessments.md`

## Quick Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
