from typing import Optional, List


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        i = 0
        while n > 0:
            bit = n % 2
            n = n >> 1
            if bit:
                result = result | (1 << (31 - i))
            i += 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(21))
    print("Running Solution...")
