from typing import Optional, List


class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n & 0xFFFFFFFF, '032b')
        return int(b[::-1], 2)

if __name__ == "__main__":
    print("Running Solution...")
