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






# Below is the solution provided (Just for future reference.)

'''
import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
'''

