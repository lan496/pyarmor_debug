# include dist/pyarmor_debug
import sys
from pathlib import Path

repo_root = Path.cwd().parent
sys.path.insert(0, str(repo_root / "dist"))

from pyarmor_debug import func

func(Path('matched'))

func(Path('unmatched'))  # -> Properly raises ValueError
