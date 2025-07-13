from typing import Optional, List


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        if n == 3: 
            return True
        return self.isPowerOfThree(n / 3)

if __name__ == "__main__":
    print("Running Solution...")
