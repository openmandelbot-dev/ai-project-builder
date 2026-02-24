# Lesson 06: File Automation

## Learning Objectives
- Traverse directories with `pathlib`.
- Organize files by extension.
- Move files safely with clear reporting.

## Core Concepts
- `Path.iterdir()` iteration.
- Extension normalization and folder creation.
- Skip directories, process files only.

## Guided Example
```python
from pathlib import Path

for item in Path(".").iterdir():
    if item.is_file():
        print(item.name)
```

## Practice Tasks
1. Group files into extension folders.
2. Add a summary counter for moved files.
3. Handle invalid target folder input.

## Exit Criteria
You can write repeatable file-organization scripts without destructive behavior.
