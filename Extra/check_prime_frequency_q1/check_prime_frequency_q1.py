from typing import Optional, List

from collections import defaultdict

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        numCount = defaultdict(int)
        
        for n in nums:
            numCount[n] += 1
        
        for key, value in numCount.items():
            if self.is_prime(value):
                return True
        return False 
    
    primeDict = {
        2:True,
        3:True,
    }
    
    def is_prime(self, n):
        if n in self.primeDict:
            return self.primeDict[n]
        if n <= 1:
            return False
        if n % 2 == 0 or n % 3 == 0:
            self.primeDict[n] = False
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                self.primeDict[n] = False
                return False
            i += 6
        self.primeDict[n] = True
        return True


if __name__ == "__main__":
    nums = [1,2,3,4,5,4]
    s = Solution()
    
    print(s.checkPrimeFrequency(nums))
    print("Running Solution...")
