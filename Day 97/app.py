from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, v, visited):
        visited[v] = True
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def count_connected_components(self):
        visited = [False] * self.V
        count = 0
        for v in range(self.V):
            if not visited[v]:
                self.dfs(v, visited)
                count += 1
        return count


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(3, 4)

print("Number of connected components:", g.count_connected_components())
