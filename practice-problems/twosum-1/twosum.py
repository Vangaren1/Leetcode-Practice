from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = { nums[i]:i for i in range(len(nums))}
        
        for i in range(len(nums)):
            curr = nums[i]
            needed = target - curr
            if needed in indexDict and indexDict[needed] != i:
                return [i, indexDict[needed]]
    
    
nums = [2,7,11,15]
target = 9

s = Solution()

print(s.twoSum(nums, target))


