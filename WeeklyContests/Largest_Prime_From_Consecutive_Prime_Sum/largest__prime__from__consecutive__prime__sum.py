from typing import Optional, List


class Solution:
    def sieve(self, n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(n + 1) if primes[i]]

    def largestPrime(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 2

        primes = self.sieve(n)
        primeSet = set(primes)
        index = 0
        s = 0
        seen = 0
        while s + primes[index] <= n:
            s += primes[index]
            if s in primeSet:
                seen = s
            index += 1
        return seen


if __name__ == "__main__":
    sol = Solution()
    assert sol.largestPrime(198) == 197
    assert sol.largestPrime(20) == 17
    assert sol.largestPrime(2) == 2
    assert sol.largestPrime(15) == 5

    print(sol.largestPrime(499968))
    print("Running Solution...")
