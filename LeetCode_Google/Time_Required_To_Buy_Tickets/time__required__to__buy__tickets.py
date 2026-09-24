from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        count = 0
        n = len(tickets)
        ptr = 0

        while tickets[k] > 0:
            if tickets[ptr] > 0:
                count += 1
                tickets[ptr] -= 1
            ptr = (ptr + 1) % n
        return count


if __name__ == "__main__":
    sol = Solution()
    tickets = [5, 1, 1, 1]
    k = 0
    print(sol.timeRequiredToBuy(tickets, k))
    print("Running Solution...")
