from typing import Optional, List


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n % 2 == 1:
            return False 
        if n < 2: 
            return False 
        
        while n & 2 != 2:
            n = n >> 1
        return n == 2

if __name__ == "__main__":
    
    s = Solution()
    
    for i in range(17):
        print(s.isPowerOfTwo(i))
    print("Running Solution...")
