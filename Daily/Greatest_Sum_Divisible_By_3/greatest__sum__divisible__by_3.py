from typing import Optional, List
import heapq


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        m1 = []
        m2 = []
        modArray = [m1, m2]
        total = 0
        for index in range(n):
            tmp = nums[index]
            m = tmp % 3
            if m != 0:
                heapq.heappush(modArray[m - 1], tmp)
            total += tmp

        modTotal = total % 3
        if modTotal == 0:
            return total
        tmp2, tmp1 = float("inf"), float("inf")
        if modTotal == 1:
            m1, m2 = m2, m1
        if len(m1) > 1:
            tmp1 = heapq.heappop(m1) + heapq.heappop(m1)
        if m2:
            tmp2 = heapq.heappop(m2)
        m = min(tmp1, tmp2)
        if m == float("inf"):
            return 0
        total -= min(tmp1, tmp2)

        return total
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 6, 5, 1, 8]
    print(sol.maxSumDivThree(nums))
    print("Running Solution...")
