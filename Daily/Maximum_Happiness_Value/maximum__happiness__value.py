from typing import Optional, List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()

        total = 0
        reduction = 0
        for _ in range(k):
            if happiness:
                h = max(0, happiness.pop() - reduction)
                total += h
                reduction += 1

        return total


if __name__ == "__main__":
    sol = Solution()
    happiness = [1, 1, 1, 1]
    k = 2

    print(sol.maximumHappinessSum(happiness, k))
    print("Running Solution...")
