# # Read input from user
# nodes = int(input("Nodes: "))
# edges = int(input("Edges: "))

# matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

# for edge in range(edges):
#     row, column = map(int, input("Edge (row, column): ").split())
#     matrix[row][column] = 1
#     matrix[column][row] = 1

# for row in range(nodes):
#     for column in range(nodes):
#         print(matrix[row][column], end=" ")
#     print()


# Read input from text file
file_name = 'adjacency_matrix_input.txt'
with open(file_name) as file:
    nodes, edges = map(int, file.readline().split())

    matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

    for line in file:
        a, b = line.split()
        matrix[int(a)][int(b)] = 1
        matrix[int(b)][int(a)] = 1

for row in range(nodes):
    for column in range(nodes):
        print(matrix[row][column], end=" ")
    print()

# with open(file_name, 'a') as file:
    # file.write('\n\nAdjacency Matrix: \n')
    # for row in range(nodes):
        # for column in range(nodes):
            # file.write(str(matrix[row][column]) + '\t')   # Write in that file
        # file.write('\n')