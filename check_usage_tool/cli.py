import os, string
from .fs import list_level
from .scanners.powershell import get_folder_size
from .printers import print_path_info
DRIVE_LIST = [f"{letter}:\\" for letter in string.ascii_uppercase]

# translate the items in a path to detailed info list
def cal_path_info(path: str) -> list[dict]:
  child_items = []
  dirs, files = list_level(path)
  for dir in dirs:
    dir_path = os.path.join(path, dir)
    try:
      size = get_folder_size(dir_path)
      child_items.append({
        "name": dir,
        "type": "directory",
        "size": size
      })
    except ValueError as ve:
      child_items.append({
        "name": dir,
        "type": "directory",
        "size": None
      })
  for file in files:
    file_path = os.path.join(path, file)
    try:
      size = os.path.getsize(file_path)
      child_items.append({
        "name": file,
        "type": "file",
        "size": size
      })
    except OSError:
      child_items.append({
        "name": file,
        "type": "file",
        "size": None
      })
  return child_items

# Main execution
def main():
  print("== Windows Drive Information ==")
  for drive in DRIVE_LIST:
    if os.path.exists(drive):
      # get and sort path info for printing
      sorted_items = sorted(
        cal_path_info(drive),
        key=lambda x: (
          x["type"] != "directory", 
          -x["size"] if x["size"] is not None else float('inf'),
        )
      )
      # print path info
      print(f"\n=== {drive} ===")
      print_path_info(sorted_items)

if __name__ == "__main__":
  main()