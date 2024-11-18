import sys
import re

def get_dim(elements):
    for element in elements:
        if element.startswith("dim"):
            match = re.search(r'dim\((\d+)\)', element)
            if match:
                return int(match.group(1))
    return None

def get_solution_matrix(elements, dim=6):
    matrix = [["." for _ in range(dim)] for _ in range(dim)]
    
    for element in elements:
        match = re.search(r'tree\((\d+),(\d+)\)', element)
        if match:
            x = int(match.group(1))-1
            y = int(match.group(2))-1
            if x >= dim or y >= dim or x < 0 or y < 0:
                print(f"Warning: tree({x+1},{y+1}) out of bounds. Ignoring it.")
                continue
            matrix[x][y] = "t"
            continue
        
        match = re.search(r'tent\((\d+),(\d+)\)', element)
        if match:
            x = int(match.group(1))-1
            y = int(match.group(2))-1
            if x >= dim or y >= dim or x < 0 or y < 0:
                print(f"Warning: tent({x+1},{y+1}) out of bounds. Ignoring it.")
                continue
            matrix[x][y] = "x"
            continue
    
    return matrix


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('No solution provided')
        sys.exit(1)
        
    filename = sys.argv[1]
    
    with open(filename, "r") as f:
        data = f.read()
    
    elements = data.split(" ")
    
    dim = get_dim(elements)     
    if dim is None:
        print("No dim found.") 
        sys.exit(1)
    
    matrix = get_solution_matrix(elements, dim=dim)
    
    # Print the matrix
    print("\n".join(["".join(row) for row in matrix]))