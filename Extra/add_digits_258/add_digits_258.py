from typing import Optional, List


class Solution:
    def addDigits(self, num: int) -> int:
        def ad(n):
            if n == 0:
                return 0
            tmp = n % 10 
            return tmp + ad(n // 10)
        while num > 9:
            num = ad(num)
        return num
        
        

    
        

if __name__ == "__main__":
    print("Running Solution...")
