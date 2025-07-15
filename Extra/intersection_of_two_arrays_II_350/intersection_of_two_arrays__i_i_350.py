from typing import Optional, List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        retVal = []
        
        for c in c1:
            
            if c in c2:
                count = min(c1[c], c2[c])
                for _ in range(count):
                    retVal.append(c)
            
        return retVal

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    
    s = Solution()
    print(s.intersect(nums1, nums2))
    
    print("Running Solution...")
