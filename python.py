import os, sys

for dir, subdirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".yaml"):
            filepath = os.path.join(dir, filename)
            filename = filename.replace("_", " ")
            with open(filepath, "w") as file:
                file.write("en: " + filename[:filename.index(".")] + "\n")