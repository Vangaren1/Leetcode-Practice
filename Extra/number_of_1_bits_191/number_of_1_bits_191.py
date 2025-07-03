from typing import Optional, List


class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        total = 0
        for c in b:
            if c == '1':
                total += 1
        return total
        

if __name__ == "__main__":
    print("Running Solution...")
