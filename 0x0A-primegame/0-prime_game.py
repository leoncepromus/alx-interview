#!/usr/bin/python3

def isWinner(x, nums):
    """Function to determine the winner of the prime game."""
    maria_wins_count = 0
    ben_wins_count = 0

    for n in nums:
        if n < 2:
            ben_wins_count += 1
            continue

        primes = sieve_of_eratosthenes(n)
        turn_maria = True

        while primes:
            current_prime = primes.pop(0)
            primes = [p for p in primes if p % current_prime != 0]

            turn_maria = not turn_maria

        if turn_maria:
            ben_wins_count += 1
        else:
            maria_wins_count += 1

    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif ben_wins_count > maria_wins_count:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(n):
    """Generates all prime numbers up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(n + 1) if sieve[i]]
