# 🎯 Day #80 of My 365 Days Coding Challenge!

## 💭 Personal Reflection

Subset Sum is one of those classic **Dynamic Programming** problems that lays the foundation for many real-world applications—**knapsack problems, financial portfolio decisions, and even AI-based decision-making**.

Today, I solved it using **Bottom-Up Dynamic Programming** to efficiently determine if a given subset sum is possible.

---

## 📚 What I Did Today

I implemented the **Subset Sum Problem** using **Tabulation (Bottom-Up DP)**.

---

## 📝 **Subset Sum Problem – Dynamic Programming Approach**

```python
def is_subset_sum(arr, target):
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]

arr = [3, 34, 4, 12, 5, 2]
target = 9
print("Subset sum possible:", is_subset_sum(arr, target))
```

---

## 💡 Key Learnings

✅ **Dynamic Programming (Bottom-Up) reduces redundancy and improves efficiency.**
✅ **Recursive relation:**

* If `arr[i] > target` → Ignore it (`dp[i][j] = dp[i-1][j]`)
* Else → Choose either including `arr[i]` or excluding it
  ✅ **Base Case:** Sum of 0 is always possible (by selecting an empty subset).
  ✅ **Useful in financial planning, decision-making, and combinatorial optimization.**

---

## 🚀 Your Turn

Can you extend this to find the **minimum subset sum difference**?

\#365DaysOfCode #CodingChallenge #SubsetSum #DynamicProgramming #Combinatorics #Optimization

---