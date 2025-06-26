from pathlib import Path
import os
import subprocess
import sys

def run_python_file(working_directory, file_path):
    file_path = Path(os.path.join(working_directory, file_path)).resolve(strict=False)
    parent = Path(working_directory).resolve(strict=True)

    # Check that the file path given is within the permitted working folder
    if not str(file_path).startswith(str(parent)):
        return f'Error: Cannot execute "../{file_path.name}" as it is outside the permitted working directory'  

    # Check if the file path exists
    if not os.path.exists(file_path):
        return f'Error: File "{file_path.name}" not found.'  
    
    # Check if the file path is a Python file
    if not str(file_path).endswith(".py"):
        return f'Error: "{file_path.name}" is not a Python file.'
    
    try:
        result = subprocess.run(
            [sys.executable, str(file_path)],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=working_directory,
            check=True
        )

        if result.stdout:
            return f"STDOUT: {result.stdout}"

        if result.stderr:
            return f"STDERR: {result.stderr}"

        return "No output produced"

    except Exception as e:
        return f'Error: executing Python file: {e}'







'''
Use subprocess.run function to execute the Python file.
Set a timeout of 30 seconds to prevent infinite execution
Capture both stdout and stderr
Set the working directory properly
Format the output to include:
The stdout (prefixed with "STDOUT:")
The stderr (prefixed with "STDERR:")
If the process exits with a non-zero code, include "Process exited with code X"
If no output is produced, return "No output produced."
If any exceptions occur during execution, catch them and return an error string:'''

