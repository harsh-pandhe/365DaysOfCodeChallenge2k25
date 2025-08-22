# 🎯 Day #111 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today I explored the fascinating world of **network flow problems**, implementing the **Maximum Flow** solution using the **Ford-Fulkerson algorithm** 🏞️.

It’s incredible how a simple approach of **finding augmenting paths** and **pushing flow** through a graph can model **real-world systems** — from water pipelines and traffic to bipartite matching and logistics networks!

---

## 📚 What I Did Today

* ✅ Built a **flow network** using an adjacency matrix
* ✅ Implemented **Ford-Fulkerson Algorithm** with **DFS** for augmenting path discovery
* ✅ Maintained and updated the **residual graph** to track remaining capacities

---

## 📝 Ford-Fulkerson Algorithm – Python Code

```python
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
```

---

## 💡 Key Learnings

* ✅ **Ford-Fulkerson** is a **greedy augmenting-path algorithm**
* ✅ It leverages a **residual graph** to manage remaining capacities
* ✅ Time Complexity (with DFS): **O(E × max\_flow)**
* ✅ More efficient variant: **Edmonds-Karp** (uses BFS → O(VE²))
* ✅ Perfect for **transportation, logistics, resource allocation, and matchmaking**

---

## 🚀 Your Turn!

Try extending this project with:

* 🧩 Using **BFS** for Edmonds-Karp implementation
* ➕ Adding **node capacities** (split node into in/out with edges)
* ⚙️ Visualizing flow paths with **arrows and live flow values**


`#365DaysOfCode` `#MaxFlow` `#FordFulkerson` `#GraphAlgorithms`
`#GreedyAlgorithm` `#NetworkFlow` `#Python` `#CodingChallenge`
`#DSA` `#AlgoLearning` `#InterviewPrep`
