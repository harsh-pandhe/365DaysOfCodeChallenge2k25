# 🎯 Day #102 of My 365 Days Coding Challenge!

## 💭 Personal Reflection
Today I dove into the world of **directed graphs** and explored how to find **Strongly Connected Components (SCCs)** — groups of nodes where **every node is reachable from every other node** in the group 🔄.  

It’s like discovering **tightly-knit communities inside a larger network** — where **influence flows freely in all directions**. From **social networks** to **compilers** to **recommendation systems**, SCCs appear everywhere!  

---

## 📚 What I Did Today
I implemented **Kosaraju’s Algorithm** to find **all SCCs** in a directed graph.  
This elegant algorithm uses **two DFS passes and a stack** to reverse the flow and **uncover hidden clusters**.

---

## 📝 Strongly Connected Components using Kosaraju’s Algorithm – Python Code

```python
from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack=None, component=None):
        visited[v] = True
        if component is not None:
            component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack, component)
        if stack is not None:
            stack.append(v)

    def transpose(self):
        gT = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                gT.add_edge(v, u)
        return gT

    def find_sccs(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        transposed = self.transpose()

        visited = [False] * self.V
        sccs = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                transposed.dfs(v, visited, component=component)
                sccs.append(component)

        return sccs


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 4)

sccs = g.find_sccs()
print("Strongly Connected Components:")
for i, comp in enumerate(sccs):
    print(f"Component {i + 1}: {comp}")

```

## 💡 Key Learnings

✅ **SCCs** are clusters where **every node can reach every other node** — like mini-strong ecosystems.

✅ **Kosaraju’s Algorithm**:

1. First DFS for finish order
2. Transpose graph
3. Second DFS in reverse order

📊 **Time Complexity**: `O(V + E)`

📌 Applications: **compiler optimization, dependency resolution, deadlock detection, and social graph analysis**.

---

## 🚀 Your Turn

Try applying **Tarjan’s Algorithm** for SCCs — it uses just **one DFS and a stack-based approach**.
Or, visualize SCCs in your favorite **social graph** and see how communities emerge!

\#️⃣ `#365DaysOfCode` `#CodingChallenge` `#SCC` `#Kosaraju` `#GraphAlgorithms`
\#️⃣ `#DirectedGraphs` `#AlgoMastery` `#InterviewPrep` `#PythonProgramming`
