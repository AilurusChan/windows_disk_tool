import sys
from .formatters import size_format

# Print path information
def print_path_info(items: list[dict]):
  dirs = [i for i in items if i["type"] == "directory"]
  files = [i for i in items if i["type"] == "file"]
  print("\n  [Directories]:")
  for dir in dirs:
    if dir["size"] is not None:
      print(f"\t- {dir["name"]} : {size_format(dir["size"])}")
    else:
      print(f"\t! {dir["name"]} : Access Denied.", file=sys.stderr)
  print("\n  [Files]:")
  for file in files:
    if file["size"] is not None:
      print(f"\t- {file["name"]} : {size_format(file["size"])}")
    else:
      print(f"\t! {file["name"]} : Access Denied.", file=sys.stderr)