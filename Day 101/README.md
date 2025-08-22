# 🎯 Day #101 of My 365 Days Coding Challenge!

## 💭 A Personal Reflection
Today I explored one of the more intriguing aspects of **graph theory** — detecting **negative weight cycles**.  
These cycles can cause serious issues in algorithms that rely on shortest paths, like in **transportation networks**, **currency exchange arbitrage**, or **scheduling systems**.  

The idea that you can loop infinitely and keep reducing your cost? Mind-bending and elegant. 🔁💸

---

## 📚 What I Did Today
I implemented the **Bellman-Ford Algorithm**, which not only finds the shortest path from a source but can also **detect negative weight cycles** in a graph.

---

## 📝 Detect Negative Cycle Using Bellman-Ford – Python Code

```python
def detect_negative_cycle(V, edges):
    dist = [0] * V

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return True

    return False

V = 3
edges = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]

if detect_negative_cycle(V, edges):
    print("⚠️ Negative weight cycle detected!")
else:
    print("✅ No negative weight cycle.")

```

## 💡 Key Learnings

* ✅ Bellman-Ford is ideal for graphs with **negative weights**.
* ✅ After **V−1 relaxations**, a **further improvement** means a **negative cycle exists**.
* ✅ **Time Complexity:** O(V × E).
* ✅ Important for **network routing**, **currency exchange arbitrage**, and **fraud detection in transactions**.

---

## 🚀 Your Turn

Try building an **input system** that detects **arbitrage opportunities in currency exchanges** using this technique!

---

\#365DaysOfCode #CodingChallenge #NegativeCycle #BellmanFord #GraphTheory #ShortestPath #AlgoMastery #PythonProgramming #InterviewPrep
