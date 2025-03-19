# 🎯 Day #64 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Graphs always seemed intimidating to me—so many nodes, edges, and complex algorithms. But today, I tackled **Dijkstra’s Algorithm**, and it finally *clicked*! 🎯  

## 📚 What I Did Today  
I implemented **Dijkstra’s Algorithm** to find the **shortest path** from a source node to all other nodes in a graph. 🚀  

---

### 📝 **Dijkstra's Algorithm Implementation**  

```python
import heapq

def dijkstra(graph, start):
    """Finds shortest paths from start node using Dijkstra's Algorithm"""
    priority_queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:  
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node}: {shortest_paths}")
```

---

## 💡 Key Learning  
✅ **Why Dijkstra?**  
- Finds **shortest paths** in **weighted graphs** 🌍  
- Uses a **priority queue (heap)** for **efficient processing**  
- Runs in **O(E log V) time complexity** (better than brute force!)  

✅ **How It Works:**  
1. **Start** at the source node with **distance 0**  
2. Use a **min-heap** to always expand the nearest unvisited node  
3. **Update distances** when a shorter path is found  
4. Repeat until all nodes are processed  

---

## ✨ Extra Touch  
🚀 **Where Dijkstra’s Algorithm Is Used?**  
- 🗺 **Google Maps** (Shortest route from A → B)  
- 🏎 **Game AI** (Pathfinding for NPCs)  
- 📡 **Network Routing** (Optimizing internet traffic)  

---

## 🚀 Your Turn  
Have you ever thought about how **Google Maps** finds the best routes so fast? Now you know! 😎  

#365DaysOfCode #CodingChallenge #Graphs #Dijkstra #ShortestPath #Python  