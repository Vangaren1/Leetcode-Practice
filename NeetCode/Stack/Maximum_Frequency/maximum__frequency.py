from typing import Optional, List
import heapq
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.groups = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        count = self.freq[val]

        self.groups[count].append(val)
        self.maxFreq = max(self.maxFreq, count)

    def pop(self) -> int:
        val = self.groups[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1
        return val


if __name__ == "__main__":
    sol = FreqStack()
    print("Running Solution...")


""" 
# solution works, but in O(log N) time and O(N) space
class FreqStack:

    def __init__(self):
        self.hq = []
        self.counter = defaultdict(int)
        self.order = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.order += 1
        heapq.heappush(self.hq, (-self.counter[val], -self.order, val))

    def pop(self) -> int:
        count, order, val = heapq.heappop(self.hq)
        self.counter[val] -= 1
        return val

"""
