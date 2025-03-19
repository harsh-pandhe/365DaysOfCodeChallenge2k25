def knapsack(W, weights, values, n):
    """Solves 0/1 Knapsack using Dynamic Programming"""
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
n = len(values)

print("Maximum Value:", knapsack(W, weights, values, n))
