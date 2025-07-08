from typing import Optional, List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def strNum(a,b):
            if a == b:
                return str(a)
            return str(a) + "->" + str(b)
        
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return str(nums[0])
        
        
        ptr1, ptr2 = 0,0
        retVal = []
        
        while ptr1 < len(nums): 
        # advance ptr2 until there is a gap or you reach the end
            while ptr2 < len(nums) -1:
                if nums[ptr2+1] - nums[ptr2] > 1:
                    break
                ptr2 += 1
            
            retVal.append(strNum(nums[ptr1], nums[ptr2]))
            
            ptr1, ptr2 = ptr2 + 1, ptr2 + 1
            
        return retVal
        
        
        pass

if __name__ == "__main__":
    s = Solution()
    
    nums = [0,2,3,4,6,8,9]
    print(s.summaryRanges(nums))
    print("Running Solution...")
