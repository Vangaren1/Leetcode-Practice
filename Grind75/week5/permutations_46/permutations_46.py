from typing import Optional, List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return None
        
        results = []
        for index in range(len(nums)):
            copyNums = nums.copy()
            curr = copyNums[index]
            copyNums.pop(index)
            if len(copyNums) == 0:
                return [[curr]]
            subPerm = self.permute(copyNums)
            
            if subPerm:
                for s in subPerm:
                    results.append( [curr] + s )
        return results

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.permute(nums))
    print("Running Solution...")
