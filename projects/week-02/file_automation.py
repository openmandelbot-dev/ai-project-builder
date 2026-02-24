"""Sort files in a directory by extension."""

from pathlib import Path
import shutil


def organize_folder(directory: Path) -> None:
    if not directory.exists() or not directory.is_dir():
        raise ValueError(f"Invalid directory: {directory}")

    moved_count = 0
    for item in directory.iterdir():
        if item.is_dir():
            continue

        suffix = item.suffix.lower().lstrip(".") or "no_extension"
        target_dir = directory / suffix
        target_dir.mkdir(exist_ok=True)
        shutil.move(str(item), str(target_dir / item.name))
        moved_count += 1

    print(f"Moved {moved_count} files in {directory}")


if __name__ == "__main__":
    target = Path(input("Folder path to organize: ").strip()).expanduser()
    organize_folder(target)
