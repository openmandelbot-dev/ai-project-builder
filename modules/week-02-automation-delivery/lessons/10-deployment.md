# Lesson 10: Deployment with GitHub Actions

## Learning Objectives
- Automate script execution on a schedule.
- Verify workflow runs and artifacts.
- Maintain a reliable milestone deployment.

## Core Concepts
- Workflow triggers: `schedule` and `workflow_dispatch`.
- Dependency installation in CI.
- Artifact upload for run outputs.

## Workflow Path
- `.github/workflows/milestone-api-job.yml`
- Script: `automation/milestone_api_job.py`

## Validation Steps
1. Run workflow manually from GitHub Actions.
2. Confirm success status.
3. Download artifact and verify `milestone-output.json`.

## Exit Criteria
You can explain and demonstrate end-to-end automated execution.
