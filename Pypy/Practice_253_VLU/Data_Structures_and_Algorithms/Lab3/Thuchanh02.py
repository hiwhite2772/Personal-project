import sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph():
    def __init__(cung, dinh):
        cung.x = dinh
        cung.graph = [[0 for column in range(dinh)] for row in range(dinh)]
    def inketqua(cung, L, a):
        print("Dinh nguon xuat phat tu:")
        for nut in range(cung.x):
            print(a, "den dinh:", nut, "do dai duong di la:", L[nut])
    def duongdinhonhat(cung, L, P):
        minimum = sys.maxsize
        min_index = -1
        for x in range(cung.x):
            if L[x] < minimum and P[x] == False:
                minimum = L[x]
                min_index = x
        return min_index
    def timduongdi(cung, a):
        L = [sys.maxsize] * cung.x
        L[a] = 0
        P = [False] * cung.x
        for cout in range(cung.x):
            u = cung.duongdinhonhat(L, P)
            P[u] = True
            for x in range(cung.x):
                if cung.graph[u][x] > 0 and P[x] == False and L[x] > L[u] + cung.graph[u][x]:
                    L[x] = L[u] + cung.graph[u][x]
        cung.inketqua(L, a)

G = nx.DiGraph()

G.add_weighted_edges_from([
    (0, 1, 3),
    (0, 3, 4),
    (1, 2, 6),
    (1, 3, 2),
    (2, 4, 4),
    (2, 5, 3),
    (3, 2, 1),
    (3, 4, 4),
    (4, 5, 5)
])

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    arrows=True
)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

g = Graph(6)   # đồ thị có hướng
g.graph = [
    [0, 3, 0, 4, 0, 0],
    [0, 0, 6, 2, 0, 0],
    [0, 0, 0, 0, 4, 3],
    [0, 0, 1, 0, 4, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0]
]
g.timduongdi(0)

