from typing import Optional, List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        total = 0

        target.insert(0, 0)

        for index in range(1, len(target)):
            tmp = target[index] - target[index - 1]
            if tmp > 0:
                total += tmp

        return total

        pass


if __name__ == "__main__":
    sol = Solution()
    target = [1, 2, 3, 2, 1]
    print(sol.minNumberOperations(target))
    print("Running Solution...")
