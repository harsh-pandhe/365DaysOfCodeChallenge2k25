# 🎯 Day #61 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Imagine you're packing for a trip 🎒. You have a limited bag size and several items with different values and weights. The challenge? **Maximize the total value** without exceeding the weight limit. This is the classic **0/1 Knapsack Problem**—a perfect example of decision-making under constraints, just like real life!  

## 📚 What I Did Today  
I implemented **0/1 Knapsack** using **Dynamic Programming** to ensure optimal efficiency. 🚀  

---

### 📝 **0/1 Knapsack Implementation**  

```python
# knapsack.py

def knapsack(W, weights, values, n):
    """Solves 0/1 Knapsack using Dynamic Programming"""
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)

print("Maximum Value:", knapsack(W, weights, values, n))
```

---

## 💡 Key Learning  
✅ **Dynamic Programming Approach:**  
- Uses a **2D DP table** where `dp[i][w]` stores the max value for `i` items and `w` weight.  
- **Transition Formula:**  
  - If an item **can be included**:  
    \[
    dp[i][w] = \max(value[i-1] + dp[i-1][w - weight[i-1]], dp[i-1][w])
    \]  
  - Else, exclude it:  
    \[
    dp[i][w] = dp[i-1][w]
    \]  

✅ **Complexity:**  
- **Time Complexity:** \(O(nW)\)  
- **Space Complexity:** \(O(nW)\), but can be optimized to \(O(W)\) with a 1D array.  

## ✨ Extra Touch  
🚀 **Applications**: Used in **budget allocation, investment decisions, and resource management**.  
🔍 **Optimization**: Try using **Memoization** or a **1D DP array** to reduce space complexity!  

## 🚀 Your Turn  
What real-life situations remind you of the **Knapsack Problem**? Let’s discuss! 🧳💡  

---

#365DaysOfCode #CodingChallenge #KnapsackProblem #DynamicProgramming #Python  