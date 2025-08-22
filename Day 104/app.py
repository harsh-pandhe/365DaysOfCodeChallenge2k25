class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)

        if u_root == v_root:
            return False

        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True


def kruskal(V, edges):
    dsu = DisjointSet(V)
    mst = []
    total_weight = 0

    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


V = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

mst, total = kruskal(V, edges)
print("MST Edges:", mst)
print("Total MST Weight:", total)
