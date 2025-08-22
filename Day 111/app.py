def dfs(residual, s, t, visited, path):
    visited[s] = True
    if s == t:
        return True

    for v in range(len(residual)):
        if not visited[v] and residual[s][v] > 0:
            path[v] = s
            if dfs(residual, v, t, visited, path):
                return True
    return False


def ford_fulkerson(graph, source, sink):
    n = len(graph)
    residual = [row[:] for row in graph]
    parent = [-1] * n
    max_flow = 0

    while True:
        visited = [False] * n
        if not dfs(residual, source, sink, visited, parent):
            break

        flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            flow = min(flow, residual[u][v])
            v = u

        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= flow
            residual[v][u] += flow
            v = u

        max_flow += flow

    return max_flow


graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]

source = 0
sink = 5
print("Maximum Flow:", ford_fulkerson(graph, source, sink))
