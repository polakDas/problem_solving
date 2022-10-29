# Initialize nodes and edges
from traceback import print_tb


nodes, edges = 0, 0

def main():
    # Read input from text file
    file_name = 'adjacency_matrix_input.txt'
    with open(file_name) as file:
        global nodes, edges
        nodes, edges = map(int, file.readline().split())

        matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

        for line in file:
            row, column = map(int, line.split())
            matrix[row][column] = 1
            matrix[column][row] = 1

        for row in range(nodes):
            for column in range(nodes):
                print(matrix[row][column], end=" ")
            print()

if __name__ == "__main__":
    main()