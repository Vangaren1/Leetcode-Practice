from typing import Optional, List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1=0
        ptr2=len(height) -1
        currVol = 0
        while ptr1 < ptr2:
            
            left = height[ptr1]
            right = height[ptr2]
            
            minh = min(left, right)
            distance = ptr2 -ptr1
            tmp= distance * minh 
            
            currVol = max( currVol, tmp)
            if right < left:
                ptr2 -=1
            else:
                ptr1 +=1
        return currVol

if __name__ == "__main__":
    print("Running Solution...")
