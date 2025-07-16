# 🎯 Day #83 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today I explored the **Coin Change Problem**, a classic in **Dynamic Programming**!
It’s fascinating how a simple real-life scenario—making change—turns into a powerful algorithmic problem with multiple variants and use cases.
This problem strengthened my understanding of **state transitions**, **unbounded knapsack**, and **recursive subproblem solving**.

---

## 📚 What I Did Today

✅ Solved two key variants of the **Coin Change Problem**:

1. **Minimum number of coins** needed to make a target amount.
2. **Total number of ways** to make the target amount using unlimited supply of coins.

---

## 📝 1. Minimum Coins to Make a Given Amount

```python
def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5]
amount = 11
print("Minimum coins needed:", min_coins(coins, amount))
```

---

## 📝 2. Total Number of Ways to Make a Given Amount

```python
def count_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    return dp[amount]

coins = [1, 2, 5]
amount = 5
print("Total number of ways:", count_ways(coins, amount))
```

---

## 💡 Key Learnings

✅ **Bottom-Up DP** helped efficiently solve both problems.
✅ **Unlimited coins** → Unbounded Knapsack Variant.
✅ Useful in:

* Payment systems & ATMs 💳
* Budget & currency optimization 💰
* Game economy balancing 🎮

✅ **Time Complexity:** O(N × amount), where N = number of coin types.
✅ **Space Complexity:** O(amount)

---

## 🚀 Your Turn

Can you enhance this by:

* Returning **the actual combinations of coins used**?
* Modifying it for **bounded coin usage**?
* Optimizing **space complexity** further?

---

\#365DaysOfCode #DynamicProgramming #CoinChange #Knapsack #Optimization #DPChallenge #CodingChallenge

---