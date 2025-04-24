import importlib.metadata
import os.path
from pathlib import Path

PROJECT_NAME: str = 'mvrgx'
PROJECT_ROOT: Path = Path(os.path.abspath(__file__)).parent
VERSION: str = importlib.metadata.version(PROJECT_NAME)
