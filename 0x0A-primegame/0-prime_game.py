#!/usr/bin/python3
"""
Prime Game

"""


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_counts = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if i in primes else 0)

    maria_wins_count = 0
    ben_wins_count = 0

    for num in nums:
        if prime_counts[num] % 2 == 0:
            ben_wins_count += 1
        else:
            maria_wins_count += 1

    if maria_wins_count > ben_wins_count:
        return "Maria"
    if ben_wins_count > maria_wins_count:
        return "Ben"
    return None


def sieve_of_eratosthenes(max_n):
    """Precompute primes using the Sieve of Eratosthenes."""
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    result = set()
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False
    for i in range(max_n + 1):
        if primes[i]:
            result.add(i)
    return result
