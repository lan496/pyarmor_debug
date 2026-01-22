from pathlib import Path


def func(root: Path):
    it = iter(root.glob(f"*.txt"))
    try:
        next(it)
    except StopIteration:
        raise ValueError from None
