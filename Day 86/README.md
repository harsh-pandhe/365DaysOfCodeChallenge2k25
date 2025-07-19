# 🎯 Day #86 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today I tackled one of the most practical graph problems: **finding the shortest path in an unweighted graph**.
What surprised me was how **Breadth-First Search (BFS)** alone can solve it efficiently and elegantly.
Whether you're building **routing systems, solving mazes, or recommending friends**, this approach forms a solid foundation.

---

## 📚 What I Did

✅ Used **BFS traversal** to calculate:

* **Shortest distance** from a source node to all other nodes
* **Actual path reconstruction** using a `parent` map

---

## 📝 BFS Implementation – Shortest Path in Unweighted Graph

```python
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
```

---

## 💡 Key Learnings

✅ **BFS guarantees shortest paths** in unweighted graphs
✅ Use a **distance dictionary** to store level info
✅ Use a **parent map** to reconstruct actual path
✅ This technique powers:

* 🔍 **Web crawlers**
* 🌐 **Social network friend suggestions**
* 🧭 **GPS navigation**
* 🔄 **Data propagation systems**

---

## 🚀 Your Turn

Try modifying this:

* 🔁 Return **all nodes at same distance from start**
* 🛣️ Print **all shortest paths** (if more than one exists)
* 📊 Extend to handle **weighted graphs** using **Dijkstra’s Algorithm**

---

\#365DaysOfCode #CodingChallenge #GraphAlgorithms #BFS #ShortestPath #UnweightedGraph #Pathfinding #Python

---