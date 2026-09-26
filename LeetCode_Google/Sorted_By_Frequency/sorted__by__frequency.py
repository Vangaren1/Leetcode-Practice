from typing import Optional, List
import heapq
from collections import defaultdict, Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        freq = [(val, key) for key, val in count.items()]
        freq.sort(key=lambda x: x[0], reverse=True)
        freq = [key * val for val, key in freq]
        return "".join(freq)

        pass


if __name__ == "__main__":
    sol = Solution()
    s = "Aabb"
    print(sol.frequencySort(s))
    print("Running Solution...")
