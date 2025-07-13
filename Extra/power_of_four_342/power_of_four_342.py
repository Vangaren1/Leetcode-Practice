from typing import Optional, List


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # print("checking {}".format(n))
        if n <= 0:
            return False
        if n == 1: 
            return True
        if n % 4 != 0 and n > 1:
            return False
        return self.isPowerOfFour(n >> 2)

if __name__ == "__main__":
    s = Solution()
    
    for i in range(32):
        print("{} {}".format(i, s.isPowerOfFour(i)))
    print("Running Solution...")
