from typing import Optional, List
import heapq
from collections import defaultdict, deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque()
        dq = deque()
        n = len(senate)

        for index, ch in enumerate(senate):
            if ch == "R":
                rq.append(index)
            else:
                dq.append(index)

        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()

            if r < d:
                rq.append(r + n)
            else:
                dq.append(r + n)

        if rq:
            return "Radiant"
        return "Dire"

        pass


if __name__ == "__main__":
    sol = Solution()
    senate = "RRDDD"
    print(sol.predictPartyVictory(senate))
    print("Running Solution...")


""" 
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rcount = senate.count("R")
        dcount = senate.count("D")
        if rcount > 0 and dcount == 0:
            return "Radiant"
        if dcount > 0 and rcount == 0:
            return "Dire"
        n = len(senate)
        canVote = [True for _ in range(n)]

        ptr = 0
        while rcount and dcount:
            curr = senate[ptr]
            if canVote[ptr]:
                if curr == "R":
                    dcount -= 1
                    # mark the first D after this so it cant vote
                    for index in range(1, n):
                        pointer = (ptr + index) % n
                        if senate[pointer] == "D" and canVote[pointer]:
                            canVote[pointer] = False
                            break
                else:
                    rcount -= 1
                    # mark the first R after this so it cant vote
                    for index in range(1, n):
                        pointer = (ptr + index) % n
                        if senate[pointer] == "R" and canVote[pointer]:
                            canVote[pointer] = False
                            break
            ptr = (ptr + 1) % n

        if rcount:
            return "Radiant"
        return "Dire"
"""
