# 🎯 Day #72 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Graphs are everywhere—social networks, navigation apps, recommendation systems—you name it! 🌍 Today, I implemented **Breadth-First Search (BFS)**, a fundamental graph traversal technique. Unlike DFS, which goes deep, BFS explores level by level, making it great for shortest path problems in unweighted graphs.  

## 📚 What I Did Today  
I implemented **BFS using a queue (FIFO approach)**. It visits all neighboring nodes before moving to the next level.  

---

### 📝 **Breadth-First Search (BFS) Implementation**  

```python
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.graph.get(node, []))

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

print("BFS Traversal:")
g.bfs(0)
```

---

## 💡 Key Learnings  
✅ **FIFO (First In, First Out) approach:**  
   - Uses a **queue** to ensure nodes are visited level by level.  
   - **Time Complexity:** **O(V + E)** (vertices + edges).  

✅ **Applications of BFS:**  
   - **Shortest path in unweighted graphs** 🛤️  
   - **Network broadcasting** 📡  
   - **Finding connected components** 🔗  
   - **AI pathfinding (e.g., in games & mazes)** 🎮  

---

## 🚀 Your Turn  
Try modifying this to **find the shortest path** between two nodes using BFS! 🔍  

#365DaysOfCode #CodingChallenge #Graphs #BFS #Algorithms  
