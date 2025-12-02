from typing import Optional, List


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        tmp = 0
        for i in range(1, k + 1):
            tmp = (tmp * 10 - 1) % k
            if tmp % k == 0:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print("results:")
    for i in range(1, 10):
        print(sol.smallestRepunitDivByK(i)),
    print("Running Solution...")
