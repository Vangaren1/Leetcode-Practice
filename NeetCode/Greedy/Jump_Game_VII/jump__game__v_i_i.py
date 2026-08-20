from typing import Optional, List
import heapq
from collections import defaultdict, deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        n = len(s)
        queue = deque()
        queue.append(0)
        farthest = 0
        while queue:
            curr = queue.popleft()

            start = max(curr + minJump, farthest + 1)
            end = min(curr + maxJump, len(s) - 1)
            for jump in range(start, end + 1):
                if s[jump] == "0":
                    if jump == len(s) - 1:
                        return True
                    queue.append(jump)
            farthest = max(farthest, end)
        return n == 1

        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.canReach("011010", 2, 3))
    print(sol.canReach("01101110", 2, 3))
    print("Running Solution...")
