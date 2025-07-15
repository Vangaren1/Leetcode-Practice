from typing import Optional, List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num in (0,1):
            return True
        
        left = 0
        right = num // 2
        
        mid = (left + right) // 2
        
        while left <= right:
            
            currSquare = mid * mid
            
            if currSquare == num:
                return True
            
            if currSquare < num:
                left = mid+1
            else: 
                right = mid-1
            
            mid = (left + right) // 2
                            
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(4))
    print(s.isPerfectSquare(3))
    print("Running Solution...")
