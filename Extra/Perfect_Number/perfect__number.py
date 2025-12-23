from typing import Optional, List


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        def divisors(n: int):
            small = []
            large = []

            i = 1
            while i * i <= n:
                if n % i == 0:
                    small.append(i)
                    if i != n // i:  # avoid duplicate when i^2 == n
                        large.append(n // i)
                i += 1

            return small + large[::-1]  # sorted

        d = divisors(num)[:-1]
        return sum(d) == num

        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkPerfectNumber(28))
    print(sol.checkPerfectNumber(7))
    print(sol.checkPerfectNumber(99999992))

    print("Running Solution...")
