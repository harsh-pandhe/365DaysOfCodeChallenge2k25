from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack=None, component=None):
        visited[v] = True
        if component is not None:
            component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack, component)
        if stack is not None:
            stack.append(v)

    def transpose(self):
        gT = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                gT.add_edge(v, u)
        return gT

    def find_sccs(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        transposed = self.transpose()

        visited = [False] * self.V
        sccs = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                transposed.dfs(v, visited, component=component)
                sccs.append(component)

        return sccs


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 4)

sccs = g.find_sccs()
print("Strongly Connected Components:")
for i, comp in enumerate(sccs):
    print(f"Component {i + 1}: {comp}")
