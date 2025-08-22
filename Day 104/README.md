# 🎯 Day #104 of My 365 Days Coding Challenge

## 🌲 Kruskal’s Algorithm – Minimum Spanning Tree (MST)

### 💭 Reflection

Today, I implemented **Kruskal’s Algorithm** — one of the most elegant ways to build a **Minimum Spanning Tree (MST)**.

What I love about it is how it **connects everything without creating cycles**, much like how **real-world networks** (roads, telecommunication, or even social connections) are optimized to be **connected yet minimal**.

At its heart, Kruskal’s Algorithm follows a simple pattern:
👉 **Sort → Pick → Union → Skip cycles** ✅

---

## 📚 What I Did

* Implemented **Kruskal’s Algorithm** for MST
* Used **Disjoint Set Union (DSU)** (Union-Find) with:

  * Path Compression
  * Union by Rank
* Constructed the MST from the lightest safe edges

---

## 📝 Code Implementation

```python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)

        if u_root == v_root:
            return False

        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True


def kruskal(V, edges):
    dsu = DisjointSet(V)
    mst = []
    total_weight = 0

    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


V = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

mst, total = kruskal(V, edges)
print("MST Edges:", mst)
print("Total MST Weight:", total)
```

---

## 💡 Key Learnings

* ✅ Kruskal’s Algorithm is **Greedy** → always takes the smallest available edge that doesn’t form a cycle.
* ✅ **Disjoint Set Union (DSU)** makes cycle detection efficient.
* ✅ Optimizations: **Path Compression + Union by Rank**.
* ⏱️ Time Complexity → **O(E log E)** (dominated by edge sorting).
* 📌 Real-world use cases:

  * Network Design (roads, fiber optics, circuits)
  * Clustering in ML
  * Minimum-cost infrastructure

---

## 🚀 Challenge for You

* Compare **Prim’s vs Kruskal’s Algorithm** on the same graph.
* Extend this implementation to:

  * Detect **redundant edges**
  * Build **minimum spanning forests**

---

\#365DaysOfCode #Kruskal #MinimumSpanningTree #GreedyAlgorithms #GraphTheory #DSU #CodingChallenge #AlgoMastery #InterviewPrep #PythonProgramming
