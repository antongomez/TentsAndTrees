import sys
import re
import clingo
import argparse


def get_dim(elements):
    for element in elements:
        if element.startswith("dim"):
            match = re.search(r"dim\((\d+)\)", element)
            if match:
                return int(match.group(1))
    return None


def get_solution_matrix(elements, dim=6):

    matrix = [["." for _ in range(dim)] for _ in range(dim)]

    for element in elements:
        match = re.search(r"tree\((\d+),(\d+)\)", element)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            if x >= dim or y >= dim or x < 0 or y < 0:
                print(f"Warning: tree({x+1},{y+1}) out of bounds. Ignoring it.")
                continue
            matrix[x][y] = "t"
            continue

        match = re.search(r"tent\((\d+),(\d+)\)", element)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            if x >= dim or y >= dim or x < 0 or y < 0:
                print(f"Warning: tent({x+1},{y+1}) out of bounds. Ignoring it.")
                continue
            matrix[x][y] = "x"
            continue

    return matrix


def solve_with_clingo(tents_file, domain_file, solutions=0):

    # Create a Control object
    ctl = clingo.Control()
    # Load the files
    ctl.load(tents_file)
    ctl.load(domain_file)
    # Ground the program
    ctl.ground([("base", [])])

    # To get all solutions
    ctl.configuration.solve.models = str(solutions)
    solutions = []
    num_solutions = 0
    with ctl.solve(yield_=True) as handle:
        for model in handle:
            num_solutions += 1
            solutions.append(model.symbols(atoms=True))

    # Check if a solution was found
    if num_solutions == 0:
        print("No solution found.")
        return

    # Check if more than one solution was found. This must be an error in the final version
    if num_solutions > 1:
        print(f"Warning: {num_solutions} solutions found.")

    # In the final version we don't need to make a loop here as we should have only one solution
    for i, solution in enumerate(solutions, start=1):
        if num_solutions > 1:
            print(f"Solution {i}")
        # Get the elements of the solution
        elements = [str(atom) for atom in solution]
        dim = get_dim(elements)

        if dim is None:
            print("No dim found in solution.")
            return

        matrix = get_solution_matrix(elements, dim=dim)

        # Print the solution
        print("\n".join(["".join(row) for row in matrix]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decode a tents puzzle from a file.")
    parser.add_argument("tents_file", help="File that contains the tents puzzle (tents.lp).")
    parser.add_argument("domain_file", help="File that contains the domain of the tents puzzle (domain.lp).")
    parser.add_argument("--solutions", type=int, help="Number of solutions to find.")

    args = parser.parse_args()
    tents_file = args.tents_file
    domain_file = args.domain_file
    solutions = args.solutions if args.solutions else 0

    solve_with_clingo(tents_file, domain_file, solutions=solutions)
