# 🎯 Day #97 of My 365 Days Coding Challenge!

💭 **A Personal Reflection:**
Today I dived into graphs to answer a fundamental question: **“How many connected components are there?”** 🧩
It’s like figuring out how many isolated social groups exist in a community — **who’s connected to whom**, and who’s out there on their own.

This challenge really made me appreciate how graph traversal helps us **map relationships and identify isolated clusters** — a concept that's useful far beyond just code.

---

## 📚 What I Did Today

I wrote a program to **count the number of connected components** in an **undirected graph** using **Depth-First Search (DFS)**.

---

## 📝 Python Implementation – Count Connected Components in a Graph

```python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = defaultdict(list)
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, v, visited):
        visited[v] = True
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def count_connected_components(self):
        visited = [False] * self.V
        count = 0
        for v in range(self.V):
            if not visited[v]:
                self.dfs(v, visited)
                count += 1
        return count

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(3, 4)

print("Number of connected components:", g.count_connected_components())
```

---

## 💡 Key Learnings

✅ A **connected component** is a set of nodes where every pair is reachable.
✅ DFS (or BFS) is used to explore each component.
✅ **Time Complexity:** O(V + E), where V = vertices and E = edges.
✅ Applications in **network analysis, clustering, image segmentation, and even Git version control!**

---

## 🚀 Your Turn

Try solving for:

* **Directed Graphs** (Strongly Connected Components).
* **Union-Find (Disjoint Set Union)** approach for large datasets.

---

### 🔖 Tags

\#365DaysOfCode #CodingChallenge #GraphTheory #ConnectedComponents #DFS #GraphTraversal #DataStructures #InterviewPrep

---