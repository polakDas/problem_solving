nodes = int(input("Nodes: "))
edges = int(input("Edges: "))

matrix = [[0 for _ in range(nodes + 1)] for _ in range(nodes + 1)]

for edge in range(edges):
    row, column = input("Edge (row, column): ").split()
    matrix[int(row)][int(column)] = 1
    matrix[int(column)][int(row)] = 1

for row in range(nodes):
    for column in range(nodes):
        print(matrix[row][column], end=" ")
    print()

# with open('adjacency_matrix_input.txt') as file:
#     a, b = file.readline().split()
#     nodes = int(a)
#     edges = int(b)

#     matrix = [[0 for _ in range(nodes)] for _ in range(nodes)]

#     for line in file:
#         a, b = line.split()
#         matrix[int(a)][int(b)] = 1
#         print(a, b)

# for row in range(nodes):
#     for column in range(nodes):
#         print(matrix[row][column], end=" ")
#     print()