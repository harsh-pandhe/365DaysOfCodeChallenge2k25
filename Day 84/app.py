def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [i for i in range(n + 1) if primes[i]]


n = 50
print(f"Prime numbers up to {n}:", sieve_of_eratosthenes(n))
