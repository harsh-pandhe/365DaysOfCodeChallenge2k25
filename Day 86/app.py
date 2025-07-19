from collections import deque, defaultdict

def bfs_shortest_path(graph, start):
    visited = set()
    distance = {}
    parent = {}
    queue = deque()

    queue.append(start)
    visited.add(start)
    distance[start] = 0
    parent[start] = None

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                parent[neighbor] = node
                queue.append(neighbor)

    return distance, parent

def reconstruct_path(parent, end):
    path = []
    while end is not None:
        path.append(end)
        end = parent[end]
    return path[::-1]

graph = defaultdict(list)
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'),
    ('C', 'E'), ('D', 'F'), ('E', 'F')
]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

start = 'A'
end = 'F'

distance, parent = bfs_shortest_path(graph, start)
path = reconstruct_path(parent, end)

print("Shortest Distance from", start, "to", end, ":", distance[end])
print("Path:", " → ".join(path))
