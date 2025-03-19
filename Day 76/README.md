# 🎯 Day #76 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Today, I took on **cycle detection in a graph** using **BFS and DFS**! 🔄 Detecting cycles is crucial in various real-world applications like **deadlock detection, network routing, and dependency resolution**. This challenge helped me **strengthen my graph traversal skills and understand how cycles impact graph structures**.  

## 📚 What I Did Today  
I implemented **cycle detection in a directed graph using DFS** and **in an undirected graph using BFS**.  

---

## 📝 **Cycle Detection Using DFS (Directed Graph)**  

```python
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    def is_cyclic(self):
        visited = {node: False for node in self.graph}
        rec_stack = {node: False for node in self.graph}

        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

print("Cycle Detected (DFS)!" if g.is_cyclic() else "No Cycle Found")
```

---

## 📝 **Cycle Detection Using BFS (Undirected Graph)**  

```python
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u) 

    def is_cyclic(self):
        visited = set()

        for start in self.graph:
            if start not in visited:
                queue = deque([(start, -1)])
                while queue:
                    node, parent = queue.popleft()
                    visited.add(node)

                    for neighbor in self.graph[node]:
                        if neighbor not in visited:
                            queue.append((neighbor, node))
                        elif parent != neighbor:
                            return True
        return False

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0) 

print("Cycle Detected (BFS)!" if g.is_cyclic() else "No Cycle Found")
```

---

## 💡 Key Learnings  
✅ **DFS Approach (Directed Graph):** Uses **recursion + a recursion stack** to detect back edges, indicating a cycle.  
✅ **BFS Approach (Undirected Graph):** Uses a **queue + parent tracking** to check if a visited node is revisited through a different path.  
✅ **Application:** Cycle detection is used in **deadlock detection, compiler dependency resolution, and blockchain DAG verification**.  

---

## 🚀 Your Turn  
Try modifying this to detect cycles in a **weighted graph** or optimize it for **large-scale networks**!  

#365DaysOfCode #CodingChallenge #GraphAlgorithms #CycleDetection #BFS #DFS  
