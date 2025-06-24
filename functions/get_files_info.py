from pathlib import Path
import os

def get_files_info(working_directory, directory=None):

    child = Path(os.path.join(working_directory, directory)).resolve(strict=True)
    parent = Path(working_directory).resolve(strict=True)
    
    if not str(child).startswith(str(parent)):
        return f'Error: Cannot list "{child}" as it is outside the permitted working directory'
    
    if not child.is_dir():
        return f'Error: "{directory}" is not a directory'
    
    output = []
    for entry in child.iterdir():
        size = entry.stat().st_size if entry.is_file() else "N/A"
        output.append(f'- {entry.name}: file_size={size} bytes, is_dir={entry.is_dir()}')

    return "\n".join(output)



# and str(parent) != str(child):