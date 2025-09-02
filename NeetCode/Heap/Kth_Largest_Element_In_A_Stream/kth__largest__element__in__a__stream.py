from typing import Optional, List

import bisect


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = nums
        self.q.sort()
        while len(self.q) > k:
            self.q.pop(0)
        self.k = k

    def add(self, val: int) -> int:
        index = bisect.bisect_left(self.q, val)
        self.q.insert(index, val)
        if len(self.q) > self.k:
            self.q.pop(0)
        return self.q[0]


if __name__ == "__main__":
    sol = KthLargest(3, [1, 2, 3, 3])
    for i in range(10):
        print(sol.add(i))

    print("Running Solution...")
