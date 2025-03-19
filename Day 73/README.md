# 🎯 Day #73 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Today's challenge brought me back to one of the core algorithms in graph theory—**Depth-First Search (DFS)**! 🌍 Unlike BFS, which explores level by level, **DFS dives deep into one branch before backtracking**. It's fascinating how this simple approach powers everything from **maze solving** 🏰 to **web crawling** 🕸️.  

## 📚 What I Did Today  
I implemented **DFS using both recursion and an iterative approach (with a stack)**.  

---

## 📝 **Recursive DFS Implementation**  

```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def dfs_recursive(self, node, visited=None):
        if visited is None:
            visited = set()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                self.dfs_recursive(neighbor, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

print("DFS Traversal (Recursive):")
g.dfs_recursive(0)
```

---

## 📝 **Iterative DFS Implementation (Using a Stack)**  

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))

graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [],
    4: [],
    5: [],
    6: []
}

print("\nDFS Traversal (Iterative):")
dfs_iterative(graph, 0)
```

---

## 💡 Key Learnings  
✅ **DFS can be implemented recursively or iteratively** (using a **stack**).  
✅ **Time Complexity:** **O(V + E)** (Vertices + Edges).  
✅ **Applications of DFS:**  
   - **Pathfinding (e.g., solving mazes 🏰)**  
   - **Cycle detection in graphs 🔄**  
   - **Topological sorting 📊**  
   - **Connected components detection**  

---

## 🚀 Your Turn  
Modify this to **detect cycles in a directed graph** using DFS! 🔄  

#365DaysOfCode #CodingChallenge #DFS #Algorithms #GraphTheory  