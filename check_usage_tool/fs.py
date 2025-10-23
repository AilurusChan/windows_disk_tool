import os
from .scanners.powershell import get_folder_size

# List directories and files at the given path
def list_level(path: str) -> tuple[list[str], list[str]]:
  files, dirs = [], []
  with os.scandir(path) as it:
    for entry in it:
      if entry.is_file():
        files.append(entry.name)
      elif entry.is_dir():
        dirs.append(entry.name)
  return dirs, files
