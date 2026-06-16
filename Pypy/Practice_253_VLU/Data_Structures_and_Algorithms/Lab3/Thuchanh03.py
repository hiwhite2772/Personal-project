import sys
import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị có hướng
G = nx.DiGraph()

# Thêm cạnh và trọng số
G.add_weighted_edges_from(
    [
        ("a", "b", 3),
        ("a", "f", 1),
        ("b", "c", 7),
        ("f", "c", 9),
        ("f", "g", 2),
        ("g", "c", 3),
        ("c", "z", 3),
        ("g", "z", 7),
    ]
)

# Vị trí các đỉnh
pos = {"a": (0, 1), "b": (1, 2), "f": (1, 0), "c": (3, 2), "g": (3, 0), "z": (4.5, 1)}

# Vẽ đồ thị
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=2000,
    arrows=True,
    font_size=12,
)

# Hiển thị trọng số
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Đồ thị có hướng")
plt.show()


class Graph:
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
                if (
                    cung.graph[u][x] > 0
                    and P[x] == False
                    and L[x] > L[u] + cung.graph[u][x]
                ):
                    L[x] = L[u] + cung.graph[u][x]

        cung.inketqua(L, a)


g = Graph(6)

g.graph = [
    [0, 3, 0, 1, 0, 0],  # a
    [0, 0, 7, 0, 0, 0],  # b
    [0, 0, 0, 0, 0, 3],  # c
    [0, 0, 9, 0, 2, 0],  # f
    [0, 0, 3, 0, 0, 7],  # g
    [0, 0, 0, 0, 0, 0],  # z
]


g.timduongdi(0)
