from typing import Optional, List


class Solution:
    def numSub(self, s: str) -> int:
        def count(n):
            return (n + 1) * n // 2

        st = s.split("0")
        total = 0

        for i in st:
            total += count(len(i))
        return total % (10**9 + 7)


if __name__ == "__main__":
    sol = Solution()
    s = "0110111"
    print(sol.numSub(s))
    print("Running Solution...")
