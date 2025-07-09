from typing import Optional, List


class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        return True

if __name__ == "__main__":
    print("Running Solution...")
