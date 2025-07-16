# 🎯 Day #82 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today, I implemented the **Floyd-Warshall Algorithm**, a powerful **Dynamic Programming** approach for solving the **All-Pairs Shortest Path** problem in weighted graphs. 🌐

It’s incredible how a few nested loops can uncover the shortest paths between every pair of nodes—something used in real-world systems like **routing protocols**, **map services**, and **transitive closure** in graphs.

---

## 📚 What I Did Today

✅ Implemented the **Floyd-Warshall Algorithm** using an **adjacency matrix** representation of the graph.
✅ Calculated the **shortest distances between every pair of vertices**, even with **negative edge weights** (as long as there are no negative cycles).

---

## 📝 Floyd-Warshall Algorithm – Python Code

```python
V = 4

INF = float('inf')

graph = [
    [0,   3,  INF, 7],
    [8,   0,   2, INF],
    [5, INF,   0,   1],
    [2, INF, INF,   0]
]

def floyd_warshall(graph):
    dist = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

shortest_paths = floyd_warshall(graph)

print("All-Pairs Shortest Distances:")
for row in shortest_paths:
    print(row)
```

---

## 💡 Key Learnings

✅ **Floyd-Warshall** uses **dynamic programming** to iteratively improve distances between all node pairs.
✅ **Time Complexity:** `O(V³)` — suitable for **dense graphs** or **smaller networks**.
✅ Supports **negative edge weights**, but **not negative cycles**.
✅ Core Idea: For every pair `(i, j)`, check if going through an intermediate node `k` yields a shorter path.

---

## 🚀 Your Turn

Try extending this algorithm to **reconstruct the actual path** using a `next[i][j]` matrix alongside the distance matrix.
This way, you can recover the route itself—not just the distance!

---

### 🔖 Hashtags

\#365DaysOfCode #FloydWarshall #DynamicProgramming #GraphAlgorithms #AllPairsShortestPath #ShortestPaths #AIPathPlanning #CodingChallenge

---