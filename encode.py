import sys
import re
import os

def search_file(pattern, dir = "./examples"):
    files = []
    for file in os.listdir(dir):
        if re.search(pattern, file):
            abs_path = os.path.abspath(os.path.join(dir, file))
            files.append(abs_path)
    return files

def process_file(file):
    with open(file, "r") as f:
        data = f.read()
    lines = data.split("\n")
    dim = len(list(lines[0]))
    print(dim)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Not regular expression provided. Example: python3 encode.py "^file.*"')
        sys.exit(1)

    pattern = sys.argv[1]

    files = search_file(pattern)

    if files:
        print("Founded files:")
        for i, file in enumerate(files, start=1):
            print(f"\tFile {i} -> {file}")
            process_file(file)
    else:
        print("Not files were found.")