import os

def add_comment_to_python_files(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r') as file:
                    content = file.read()
                with open(file_path, 'w') as file:
                    file.write("# Sanu K Joseph\n" + content) #comment to add at top of each files

root_folder = "/home/mca/sanu/college-python" # Change this to the root folder where your .py files are located
add_comment_to_python_files(root_folder)


