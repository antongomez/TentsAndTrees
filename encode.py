import sys
import re
import os


def search_file(pattern, dir="./examples"):
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

    # Get the dimension of the matrix
    dim = len(list(lines[0]))
    print(f"\tProblem dimension: {dim} x {dim}")

    trees = []
    rows = []
    cols = []

    # Process first dim rows to find tree positions
    for row_index, line in enumerate(lines[:dim]):
        for col_index, char in enumerate(line):
            if char == "t":
                trees.append((row_index, col_index))

    # Process the next two rows to finds tents in each column and row
    for col_index, n_tents in enumerate(lines[dim].split(" ")[:dim]):
        cols.append((col_index, n_tents))
    for row_index, n_tents in enumerate(lines[dim + 1].split(" ")[:dim]):
        rows.append((row_index, n_tents))

    # Write the facts to a file
    lp_filename = os.path.splitext(file)[0] + ".lp"
    with open(lp_filename, "w") as lp_file:

        # Write the dim fact
        lp_file.write("% Dimension\n")
        lp_file.write(f"dim({dim}).\n")

        # Write trees facts with the trees in same row in same line
        lp_file.write("\n% Trees\n")
        actual_row = 0
        for tree in trees:
            while tree[0] != actual_row:
                lp_file.write("\n")
                actual_row += 1
            lp_file.write(f"tree({tree[0]},{tree[1]}). ")

        # Write the column facts
        lp_file.write("\n\n% Columns\n")
        for col in cols:
            lp_file.write(f"col({col[0]},{col[1]}). ")

        # Write the row facts
        lp_file.write("\n\n% Rows\n")
        for row in rows:
            lp_file.write(f"row({row[0]},{row[1]}). ")

    print(f"\tClingo facts written to {lp_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('No regular expression provided. Example: python3 encode.py "^file.*"')
        sys.exit(1)

    pattern = sys.argv[1]

    files = search_file(pattern)

    if files:
        for i, file in enumerate(files, start=1):
            print(f"File {i} -> {file}")
            process_file(file)
    else:
        print("No files found.")
