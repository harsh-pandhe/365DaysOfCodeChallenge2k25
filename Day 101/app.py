def detect_negative_cycle(V, edges):
    dist = [0] * V

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return True

    return False

V = 3
edges = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]

if detect_negative_cycle(V, edges):
    print("⚠️ Negative weight cycle detected!")
else:
    print("✅ No negative weight cycle.")
