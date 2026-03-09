from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = ""
        for index, val in enumerate(nums):
            result += "0" if val[index] == "1" else "1"
        return result


if __name__ == "__main__":
    sol = Solution()
    nums = ["00", "01"]
    print(sol.findDifferentBinaryString(nums))
    print("Running Solution...")
