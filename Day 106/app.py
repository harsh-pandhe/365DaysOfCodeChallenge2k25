import heapq
from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def dijkstra(self, source):
        dist = {}
        visited = set()
        min_heap = [(0, source)]

        while min_heap:
            curr_dist, u = heapq.heappop(min_heap)

            if u in visited:
                continue
            visited.add(u)
            dist[u] = curr_dist

            for neighbor, weight in self.adj[u]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (curr_dist + weight, neighbor))

        return dist


g = Graph()
edges = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("C", "E", 10),
    ("D", "E", 2),
    ("D", "Z", 6),
    ("E", "Z", 3),
]

for u, v, w in edges:
    g.add_edge(u, v, w)

source = "A"
shortest_paths = g.dijkstra(source)

print(f"Shortest paths from '{source}':")
for node in sorted(shortest_paths):
    print(f"{source} → {node} = {shortest_paths[node]}")
