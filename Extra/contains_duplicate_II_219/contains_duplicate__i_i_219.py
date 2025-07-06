from typing import Optional, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ptr1 = 0
        ptr2 = k
        seen = set()
        
        for i in range(min(k, len(nums))):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            
        if len(nums) < k:
            return False
            
        while  ptr2 < len(nums):
            curr = nums[ptr2]
            if curr in seen:
                return True
            seen.add(curr)
            seen.remove(nums[ptr1])
            ptr2 += 1
            ptr1 += 1

        
        return False
    
    
if __name__ == "__main__":
    s = Solution()
    
    # nums = [1,2,3,1]
    # k = 3
    # assert s.containsNearbyDuplicate(nums, k) == True
    
    # nums = [1,0,1,1]
    # k = 1
    # assert s.containsNearbyDuplicate(nums, k) == True
    
    nums = [1,2,3,1,2,3]
    k = 2
    assert s.containsNearbyDuplicate(nums, k) == False
    print("Running Solution...")
