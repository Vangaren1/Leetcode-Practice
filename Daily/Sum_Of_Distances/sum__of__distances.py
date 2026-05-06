from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indexMap = defaultdict(list)
        pre = defaultdict(list)
        for index, num in enumerate(nums):
            indexMap[num].append(index)
            pre[num].append(index)
            if len(pre[num]) > 1:
                pre[num][-1] += pre[num][-2]
        print(indexMap)
        print(pre)
        n = len(nums)
        results = [0] * n

        for index, num in enumerate(nums):
            idx = indexMap[num]
            if len(idx)>1:
                

        return results
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 1, 1, 2]
    print(sol.distance(nums))
    print("Running Solution...")
