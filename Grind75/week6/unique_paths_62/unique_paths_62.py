from typing import Optional, List

import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = (m-1)
        b = (n-1)
        return math.comb(a+b, a)
    
if __name__ == "__main__":
    s = Solution()
    m = 3
    n = 7
    expected = 28
    
    print(s.uniquePaths(m,n))
    
    m=3
    n=2
    expected = 3
    print(s.uniquePaths(m,n))
    
    print("Running Solution...")
