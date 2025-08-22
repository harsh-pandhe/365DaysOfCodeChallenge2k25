# 🎯 Day #106 of My 365 Days Coding Challenge!

## 💭 **A Personal Reflection:**  
Today I tackled one of the most powerful and widely used graph algorithms — **Dijkstra’s Algorithm** for finding the shortest path in a graph with **non-negative weighted edges**.  

Whether you're navigating GPS routes, optimizing delivery paths, or building game maps — this algorithm is everywhere.  
And honestly, watching it work feels like magic ✨ as it always chooses the **greedy but right** step forward.  

---

## 📚 What I Did Today:
✅ Built a **graph using an adjacency list**  
✅ Implemented **Dijkstra’s Algorithm** using a **min-heap (priority queue)** to compute the shortest path efficiently  

---

## 📝 Dijkstra's Algorithm – Python Code

```python
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
    ("E", "Z", 3)
]

for u, v, w in edges:
    g.add_edge(u, v, w)

source = "A"
shortest_paths = g.dijkstra(source)

print(f"Shortest paths from '{source}':")
for node in sorted(shortest_paths):
    print(f"{source} → {node} = {shortest_paths[node]}")
```

## 💡 Key Learnings:

* ✅ Dijkstra’s is a **greedy algorithm** — always picks the minimum cost path first
* ✅ Works only when **all edge weights are non-negative**
* ✅ Time Complexity: **O((V + E) log V)** with **min-heap + adjacency list**
* ✅ Used in **Google Maps, network routing, resource optimization**, and **robot pathfinding**

---

## 🚀 Your Turn:

Try this out:

* 🔄 Convert it to a **directed graph**
* ⚙️ Add a function to print the actual **shortest path trace**
* 🔁 Compare with **Bellman-Ford** for graphs with negative edges

---

🔖 **#365DaysOfCode #GraphAlgorithms #Dijkstra #ShortestPath #WeightedGraph #PythonCoding #AlgorithmChallenge #GreedyAlgorithms #InterviewPrep**
