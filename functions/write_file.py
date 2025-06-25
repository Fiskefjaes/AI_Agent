from pathlib import Path
import os

def write_file(working_directory, file_path, content):
    file_path = Path(os.path.join(working_directory, file_path)).resolve(strict=False)
    parent = Path(working_directory).resolve(strict=True)

    if not str(file_path).startswith(str(parent)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        os.makedirs(file_path.parent, exist_ok=True)
    except Exception as e:
        return f'Error: Failed to create directory "{file_path.parent}": {e}'
    
    try:
        with file_path.open("w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: Failed to write to "{file_path}": {e}'
    else:
        return f'Successfully wrote to \"{file_path}\" ({len(content)} characters written)'

