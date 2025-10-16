from typing import Optional, List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        n = len(nums)

        last = 0
        for i in range(n):
            leftToRight = nums[i][i]
            rightToLeft = nums[i][n - i - 1]
            if is_prime(leftToRight):
                last = max(leftToRight, last)
            if is_prime(rightToLeft):
                last = max(rightToLeft, last)
        return last


if __name__ == "__main__":
    sol = Solution()
    nums = [[1, 2, 3], [5, 6, 7], [9, 10, 11]]
    print(sol.diagonalPrime(nums))
    print("Running Solution...")
