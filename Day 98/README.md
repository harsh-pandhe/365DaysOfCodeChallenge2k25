# 🎯 Day #98 – Check if a Graph is Bipartite

## 💭 **Personal Reflection**
Today’s challenge made me revisit one of the most elegant concepts in graph theory — checking if a **graph is bipartite** 🎨🔗.
A bipartite graph can be divided into two groups such that no two connected nodes are in the same group — kinda like forming two teams with no internal rivalries 😄.

It’s amazing how **simple coloring logic** can uncover deep structure. This challenge felt like solving a social puzzle using code!

---

## 📚 What I Did

I implemented a function to **check if an undirected graph is bipartite** using **Breadth-First Search (BFS)** and **two-coloring**.

---

## 📝 Implementation – Python Code

```python
from collections import deque, defaultdict

def is_bipartite(graph, V):
    color = [-1] * V  # -1: uncolored, 0: red, 1: blue

    for start in range(V):
        if color[start] == -1:  # Not yet visited
            queue = deque([start])
            color[start] = 0

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False  # Same color on both ends → not bipartite
    return True

# Example usage:
# Graph:
# 0---1
# |   |
# 3---2

graph = defaultdict(list)
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
V = 4

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print("Is the graph bipartite?", is_bipartite(graph, V))  # Output: True ✅
```

---

## 💡 Key Learnings

* ✅ Bipartite graphs can be **2-colored without conflict**.
* ✅ If a **cycle with odd length** exists, the graph is **not bipartite**.
* ✅ Use **BFS** (or DFS) to assign colors level by level.
* ✅ Time Complexity: **O(V + E)** — efficient even for large graphs.
* ✅ Useful in **matching problems, scheduling, and social networks**.

---

## 🚀 Your Turn

* Try modifying the code to **detect odd-length cycles**.
* Extend the logic to **graph coloring problems with more than 2 colors**.

---

\#365DaysOfCode #CodingChallenge #GraphTheory #BipartiteGraph #BFS #Coloring #DataStructures #InterviewPrep #AlgorithmDaily

---