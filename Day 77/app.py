import sys

N = 4

dist = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]

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
