# 🎯 Day #74 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Today, I tackled **Prim’s Algorithm**—a classic greedy algorithm for finding the **Minimum Spanning Tree (MST)** of a weighted graph! 🌲✨ It's fascinating how this algorithm efficiently connects all nodes with the **minimum possible total edge weight**, making it useful in **network design, circuit wiring, and transportation systems**. 🚆🔌  

## 📚 What I Did Today  
I implemented **Prim’s Algorithm using a priority queue (min-heap)** to efficiently extract the minimum-weight edges.  

---

## 📝 **Prim’s Algorithm Implementation (Using Min-Heap)**  

```python
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
```

---

## 💡 Key Learnings  
✅ **Prim’s Algorithm grows the MST step by step**, always picking the smallest edge that connects to an unvisited node.  
✅ **Time Complexity:** **O(E log V)** (because of the min-heap operations).  
✅ **Difference from Kruskal’s Algorithm:**  
   - **Prim’s Algorithm** works **greedily by growing the MST from a starting node**.  
   - **Kruskal’s Algorithm** sorts all edges and **builds the MST using union-find**.  

---

## 🚀 Your Turn  
Modify this implementation to **use an adjacency matrix instead of an adjacency list**! 📊  

#365DaysOfCode #CodingChallenge #GraphAlgorithms #PrimMST #GreedyAlgorithms  