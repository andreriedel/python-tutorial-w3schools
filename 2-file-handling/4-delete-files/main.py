import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

os.rmdir("my-folder") # only works with empty folders
