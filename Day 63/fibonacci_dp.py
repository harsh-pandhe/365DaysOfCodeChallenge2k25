def fibonacci(n):
    """Finds the nth Fibonacci number using Dynamic Programming"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


n = 10
print(f"Fibonacci({n}):", fibonacci(n))
