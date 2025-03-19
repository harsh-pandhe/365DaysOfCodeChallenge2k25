import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))

    def prim_mst(self, start):
        min_heap = [(0, start)]
        visited = set()
        mst_weight = 0
        mst_edges = []

        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited.add(u)
            mst_weight += weight
            if len(visited) > 1:
                mst_edges.append((u, weight))

            for edge_weight, v in self.graph.get(u, []):
                if v not in visited:
                    heapq.heappush(min_heap, (edge_weight, v))

        return mst_weight, mst_edges


g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 6)

mst_weight, mst_edges = g.prim_mst(0)
print("Minimum Spanning Tree Edges:", mst_edges)
print("Total MST Weight:", mst_weight)
