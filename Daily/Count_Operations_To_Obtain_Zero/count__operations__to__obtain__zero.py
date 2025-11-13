from typing import Optional, List


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0

        while num1 != 0 and num2 != 0:
            if num1 <= num2:
                num2 -= num1
            else:
                num1 -= num2
            count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
