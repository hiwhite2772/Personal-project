# câu a
n = 8

A = [[0 for _ in range(n)] for _ in range(n)]

edges = [
    (0,1),
    (0,3),
    (1,2),
    (1,5),
    (5,3),
    (5,6),
    (3,4),
    (6,2),
    (6,4),
    (2,7),
    (4,7)
]

for u, v in edges:
    A[u][v] = 1

print("Ma trận kề:")

for row in A:
    print(*row)

# câu b
import sys

class Graph:
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for _ in range(dinh)] for _ in range(dinh)]

    def inketqua(self, L, a):
        print("Dinh nguon:", a)
        for nut in range(self.x):
            print("Den dinh", nut, "co do dai:", L[nut])

    def duongdinhonhat(self, L, P):
        minimum = sys.maxsize
        min_index = -1

        for x in range(self.x):
            if L[x] < minimum and P[x] == False:
                minimum = L[x]
                min_index = x

        return min_index

    def timduongdi(self, a):
        L = [sys.maxsize] * self.x
        L[a] = 0

        P = [False] * self.x

        for _ in range(self.x):

            u = self.duongdinhonhat(L, P)
            P[u] = True

            for x in range(self.x):
                if (
                    self.graph[u][x] > 0
                    and P[x] == False
                    and L[x] > L[u] + self.graph[u][x]
                ):
                    L[x] = L[u] + self.graph[u][x]

        self.inketqua(L, a)


g = Graph(6)

g.graph = [
    [0, 2, 0, 5, 0, 0],  # a
    [0, 0, 7, 0, 1, 0],  # b
    [0, 0, 0, 0, 0, 1],  # c
    [0, 0, 0, 0, 6, 0],  # d
    [0, 0, 3, 0, 0, 2],  # e
    [0, 0, 0, 0, 0, 0],  # z
]

g.timduongdi(0)