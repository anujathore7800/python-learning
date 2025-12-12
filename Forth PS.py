import os

path = "/"

try:
    entries = os.listdir(path)
    for name in entries:
        full_path = os.path.join(path, name)
        if os.path.isfile(full_path):
            print(name)
except Exception as e:
    print("Error:", e)
