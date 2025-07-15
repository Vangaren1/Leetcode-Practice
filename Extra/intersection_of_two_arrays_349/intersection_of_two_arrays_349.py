from typing import Optional, List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        set2 = set()
        
        for num in nums1:
            set1.add(num)
            
        for num in nums2:
            if num in set1:
                set2.add(num)
        
        return [ n for n in set2]

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    
    s = Solution()
    print(s.intersection(nums1, nums2))
    print("Running Solution...")
