import os

def rename_files(base_dir, type_of_file, new_type_of_file)
    for dir, subdirs, files in os.walk("."):
        print(f"{dir}\n {subdirs}\n {files}")
        for file in files:
            if file.endswith(type_of_file):
                os.rename(file, file.replace(f".{type_of_file}", f".{new_type_of_file}"))

rename_files("", "", "")