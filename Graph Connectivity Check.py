import networkx as nx
import matplotlib.pyplot as plt
incidence_matrix = []
with open("matrix_of_incendence43.txt") as f:
    for line in f:
        row = line.split()
        incidence_matrix.append(row)
num_rows = len(incidence_matrix)
num_cols = len(incidence_matrix[0])
t_matrix = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
# loop through each element in the# original matrix and insert it into the
# transposed matrix
for i in range(num_rows):
    for j in range(num_cols):
        t_matrix[j][i] = incidence_matrix[i][j]
edges = []
graph_matrix = [[0 for _ in range(num_rows)] for _ in range(num_rows)]
m = 0
for i in range(len(t_matrix)):
    edge = []
    for j in range(len(t_matrix[0])):
        if t_matrix[i][j] == "1":
            edge.append(j)
            print(j, end = " ")
    if len(edge) == 1:
        edge.append(edge[0])
        start = edge[0]
        graph_matrix[start][start] += 1
    else:
        start = edge[0]
        finish = edge[1]
        if graph_matrix[start][finish] == 0:
            m += 1
        graph_matrix[start][finish] += 1
        graph_matrix[finish][start] += 1
    print()
    edges.append(edge)
n = num_rows
if m > (n - 1) * (n - 2) / 2:
    print("Connected graph by Theorem")
else:
    print("The condition of the theorem is not satisfied")
print(f"Number of vertices: {n}")
print(f"Number of edges excluding loops and duplicate edges: {m}")
for i in range(n):
    print(f"vertice {i}: ", end=" ")
    for j in range(n):
        if graph_matrix[i][j] > 0:
            print(f"{j} ({graph_matrix[i][j]} times)", end=" ")
    print()
#G = nx.Graph()
G = nx.MultiGraph()
for e in edges:
    G.add_edge(*e)
nx.draw_networkx(G)
plt.show()



# n = 5
# m = 15
# (n - 1) * (n - 2) / 2 = 4 * 3 / 2 = 6

# m = 6

