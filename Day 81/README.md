# 🎯 Day #81 of My 365 Days Coding Challenge!

## 💭 Personal Reflection

Today, I explored **Topological Sorting**—a powerful concept in **Directed Acyclic Graphs (DAGs)**. 📈
It’s used to determine the **correct order of tasks** when dependencies exist (like build systems, task schedulers, or course prerequisites).

Understanding how to sort nodes **linearly while respecting dependencies** felt like solving a mini puzzle 🧩.

---

## 📚 What I Did Today

I implemented **Topological Sort using both DFS and Kahn’s Algorithm (BFS)** to explore two different approaches.

---

## 📝 Topological Sort Using DFS (Recursive Approach)

```python
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.topological_sort_util(neighbor, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = set()
        stack = []

        for node in list(self.graph):
            if node not in visited:
                self.topological_sort_util(node, visited, stack)

        return stack[::-1]

g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

order = g.topological_sort()
print("Topological Sort (DFS):", order)
```

---

## 📝 Topological Sort Using Kahn’s Algorithm (BFS)

```python
from collections import defaultdict, deque

def kahn_topological_sort(V, edges):
    graph = defaultdict(list)
    in_degree = [0] * V

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(V) if in_degree[i] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for neighbor in graph[u]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != V:
        return "Cycle Detected - Topological sort not possible"
    
    return topo_order

V = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

print("Topological Sort (Kahn's Algorithm):", kahn_topological_sort(V, edges))
```

---

## 💡 Key Learnings

✅ **Topological Sort** is only valid for **DAGs (Directed Acyclic Graphs)**.
✅ **DFS-based** approach uses **postorder traversal** with a stack.
✅ **Kahn's Algorithm** is an **indegree-based BFS** that detects cycles too.
✅ Real-world applications include:

* 📦 **Build systems** (e.g. Makefile, Gradle)
* 📚 **Course scheduling systems**
* ⚙️ **Job/task scheduling**
* 🔁 **Dependency resolution**

---

## 🚀 Your Turn

Try applying topological sort to **detect circular dependencies in course schedules or software builds!**

---

\#365DaysOfCode #CodingChallenge #TopologicalSort #GraphAlgorithms #DFS #KahnsAlgorithm #DAG

---