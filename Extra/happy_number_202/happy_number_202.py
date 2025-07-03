from typing import Optional, List


class Solution:
    def isHappy(self, n: int) -> bool:
        def convert(i):
            s = str(i)
            total = 0
            for c in s:
                total += int(c)**2
            return total
        
        seen = set()
        
        while True:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = convert(n)
        return False
    

if __name__ == "__main__":
    
    s = Solution()
    
    assert s.isHappy(19) == True
    assert s.isHappy(2) == False
    print("Running Solution...")
