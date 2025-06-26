# from subdirectory.filename import function_name
from functions.run_python import run_python_file


print(f'{run_python_file("calculator", "main.py")}')
print(f'{run_python_file("calculator", "tests.py")}')
print(f'{run_python_file("calculator", "../main.py")}')
print(f'{run_python_file("calculator", "nonexistent.py")}')




'''
print(f'{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}')
print(f'{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')
print(f'{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}')





print(f'{get_file_content("calculator", "main.py")}')
print(f'{get_file_content("calculator", "pkg/calculator.py")}')
print(f'{get_file_content("calculator", "/bin/cat")}') #(this should return an error string)




print(f"{get_file_content("calculator", "lorem.txt")}")


print(f"{get_files_info("calculator", ".")}")
print(f"{get_files_info("calculator", "pkg")}")
print(f"{get_files_info("calculator", "/bin")}")
print(f"{get_files_info("calculator", "../")}")'''

