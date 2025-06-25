from pathlib import Path
import os


def get_file_content(working_directory, file_path):

    file_path = Path(os.path.join(working_directory, file_path)).resolve(strict=True)
    #file_path = Path(file_path).resolve(strict=True)
    parent = Path(working_directory).resolve(strict=True)
    
    if not str(file_path).startswith(str(parent)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
                
    
    if not file_path.is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'   

    try:
        MAX_CHARS = 10000

        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if len(file_content_string) > 9999:
                return file_content_string + f"[...File '{file_path}' truncated at 10000 characters]"
            else:
                return file_content_string
            
    
    except Exception as e:
        return f"Error: Something went wrong: {e}"
