import os

# Get folder size
def get_folder_size(path: str) -> int:
  cmd = (
    f"powershell -Command "
    f"\"(Get-ChildItem '{path}' -Recurse -Force | "
    f"Measure-Object -Property Length -Sum).Sum\""
  )
  print(f"\r\033[Kcalculating {path} ...", end="", flush=True)
  
  stream = os.popen(cmd)
  output = stream.read().strip()
  try:
    return int(output)
  except ValueError:
    raise ValueError("access denied or invalid path.")