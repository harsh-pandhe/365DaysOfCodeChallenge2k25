# 🎯 Day #77 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Today, I tackled the **Travelling Salesman Problem (TSP)** using **Dynamic Programming + Bitmasking**! 🚀  
TSP is a classic optimization problem in which a salesman must visit **N cities exactly once** and return to the starting city while minimizing the total travel cost.  

This challenge **strengthened my understanding of bitmasking, recursion, and DP**—essential techniques for solving complex optimization problems.  

---

## 📚 What I Did Today  
I implemented the **Held-Karp algorithm** (Dynamic Programming with Bitmasking) to solve TSP efficiently in **O(N² * 2^N)** time complexity.  

---

## 📝 **Travelling Salesman Problem (TSP) – DP + Bitmasking**  

```python
import sys

N = 4

dist = [
    [0, 10, 15, 20],  
    [10, 0, 35, 25],  
    [15, 35, 0, 30], 
    [20, 25, 30, 0]  
]

dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(city, mask):
    if mask == (1 << N) - 1: 
        return dist[city][0]  

    if dp[city][mask] != -1:
        return dp[city][mask]

    min_cost = sys.maxsize

    for next_city in range(N):
        if mask & (1 << next_city) == 0:
            new_cost = dist[city][next_city] + tsp(next_city, mask | (1 << next_city))
            min_cost = min(min_cost, new_cost)

    dp[city][mask] = min_cost
    return min_cost

min_travel_cost = tsp(0, 1)
print("Minimum Travel Cost:", min_travel_cost)
```

---

## 💡 Key Learnings  
✅ **Dynamic Programming + Bitmasking** optimizes TSP from **O(N!) → O(N² * 2^N)**.  
✅ **Base Case:** If all cities are visited, return to the start.  
✅ **Recursive Case:** Try all possible unvisited cities and take the minimum cost.  
✅ **Memoization:** Avoid recomputing the same subproblems.  

---

## 🚀 Your Turn  
Can you optimize this further using **Branch & Bound** or **Genetic Algorithms**?  

#365DaysOfCode #CodingChallenge #TSP #DynamicProgramming #Bitmasking #Optimization  
