def longest_increasing_subsequence(arr):
    """Finds the length of the Longest Increasing Subsequence using DP"""
    n = len(arr)
    if n == 0:
        return 0

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Length of LIS:", longest_increasing_subsequence(arr))
