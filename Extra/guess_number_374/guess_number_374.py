from typing import Optional, List


class Solution:
    def guess(self, n):
        pick =7
        if n == pick:
            return 0
        if n > 7:
            return -1
        return 1
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n+1
        curr = (n+1) // 2
        check = self.guess(curr)
        while ( check != 0 and left < right):
            
            if check == -1:
                right = curr -1
            else:
                left = curr +1
            
            curr = (left + right) // 2
            check = self.guess(curr)
            
            
        return curr

if __name__ == "__main__":
    s = Solution()
    print(s.guessNumber(20))
    print("Running Solution...")
