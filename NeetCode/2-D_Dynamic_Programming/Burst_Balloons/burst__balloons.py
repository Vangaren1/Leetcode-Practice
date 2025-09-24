from typing import Optional, List
import heapq


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        if len(nums) == 1:
            return nums[0]

        # find min index
        m = float("inf")
        idx = -1
        for index, num in enumerate(nums):
            if num < m:
                m = num
                idx = index

        # pad the left and right
        nums.insert(0, 1)
        nums.append(1)
        idx += 1

        total = nums[idx - 1] * nums[idx] * nums[idx + 1]
        left = nums[1:idx]
        right = nums[idx + 1 : -1]
        mleft = self.maxCoins(left)
        mright = self.maxCoins(right)
        total += mleft * mright

        print(f"min index: {idx}, total: {total}")
        return total


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 2, 3, 7]
    print(sol.maxCoins(nums))
    print("Running Solution...")
