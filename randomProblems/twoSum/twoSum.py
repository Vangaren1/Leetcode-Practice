from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valDict = { target-nums[n]:n for n in range(len(nums))}
        for index in range(len(nums)):
            targetIndex = valDict[target - nums[index]]
            if targetIndex != index:
                return [index, targetIndex]
            
        return 0
        pass 
    
s = Solution()

nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))
