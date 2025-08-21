from collections import deque, defaultdict


def is_bipartite(graph, V):
    color = [-1] * V  # -1: uncolored, 0: red, 1: blue

    for start in range(V):
        if color[start] == -1:  # Not yet visited
            queue = deque([start])
            color[start] = 0

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False  # Same color on both ends → not bipartite
    return True


# Example usage:
# Graph:
# 0---1
# |   |
# 3---2

graph = defaultdict(list)
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
V = 4

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print("Is the graph bipartite?", is_bipartite(graph, V))  # Output: True ✅
