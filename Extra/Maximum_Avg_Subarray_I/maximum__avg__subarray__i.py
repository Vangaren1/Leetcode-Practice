from typing import Optional, List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums) / 1

        start = 0
        end = k
        total = sum(nums[:k])
        best = total / k

        while end < len(nums):
            total -= nums[start]
            start += 1
            total += nums[end]
            end += 1
            best = max(total / k, best)
        return best


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(sol.findMaxAverage(nums, k))
    print("Running Solution...")
