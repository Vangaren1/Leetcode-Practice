from typing import Optional, List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = 0
        for n in nums:
            total += n
            
        if total %2 == 1:
            return False
        goal = total // 2
        numSet = set()
        numSet.add(0)
        
        for index in range(len(nums)-1, -1, -1):
            newSet = numSet.copy()
            for s in newSet:
                numSet.add(s + nums[index])
            if goal in numSet:
                    return True
        return False 
        


if __name__ == "__main__":
    s = Solution()
    nums = [2,2,1,1]
    print(s.canPartition(nums))
    
    nums = [1,2,3,5]
    print(s.canPartition(nums))
    
    print("Running Solution...")
