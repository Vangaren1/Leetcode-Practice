from typing import Optional, List
from collections import defaultdict
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        target = math.ceil(n / 2)
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
            if count[n] >= target:
                return n

        pass

if __name__ == "__main__":
    t = [2,2,1,1,1,2,2,]
    s = Solution()
    print(s.majorityElement(t))
    print("Running Solution...")
