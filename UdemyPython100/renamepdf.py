import os

def renamepdf(path):
    for filename in os.listdir(path):
        if filename.endswith(".pdf"):
            os.rename(os.path.join(path, filename), os.path.join(path, filename.replace("+", "_")))
        # if the file name is a folder
        elif filename.endswith("/"):
            os.rename(os.path.join(path, filename), os.path.join(path, filename.replace("+", "_")))

renamepdf("./")