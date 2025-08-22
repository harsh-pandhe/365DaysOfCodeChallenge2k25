from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, u, visited, parent, low, disc, ap, bridges):
        children = 0
        visited[u] = True
        disc[u] = low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:
                children += 1
                self.dfs(v, visited, u, low, disc, ap, bridges)
                low[u] = min(low[u], low[v])

                if parent != -1 and low[v] >= disc[u]:
                    ap[u] = True

                if low[v] > disc[u]:
                    bridges.append((u, v))

            elif v != parent:
                low[u] = min(low[u], disc[v])

        if parent == -1 and children > 1:
            ap[u] = True

    def find_critical_points(self):
        visited = [False] * self.V
        disc = [float("inf")] * self.V
        low = [float("inf")] * self.V
        ap = [False] * self.V
        bridges = []

        for u in range(self.V):
            if not visited[u]:
                self.dfs(u, visited, -1, low, disc, ap, bridges)

        articulation_points = [u for u, is_ap in enumerate(ap) if is_ap]
        return articulation_points, bridges


g = Graph(5)
edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)]
for u, v in edges:
    g.add_edge(u, v)

aps, bridges = g.find_critical_points()
print("Articulation Points:", aps)
print("Bridges:", bridges)
