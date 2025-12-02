from typing import Optional, List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last = float("-inf")

        total = 0

        for time in timeSeries:
            step = time - last
            if step < duration:
                total += step
            else:
                total += duration
            last = time

        return total
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPoisonedDuration([1, 4], 2))
    print(sol.findPoisonedDuration([1, 2], 2))
    print("Running Solution...")
