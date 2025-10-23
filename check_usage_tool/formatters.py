# Format size in bytes to human-readable format
def size_format(size: int) -> str:
  match size:
    case _ if size > 1024 ** 3:
      return f"{size / 1024 ** 3:.2f} GB"
    case _ if size > 1024 ** 2:
      return f"{size / 1024 ** 2:.2f} MB" 
    case _ if size > 1024:
      return f"{size / 1024:.2f} KB"
    case _:
      return f"{size} bytes"