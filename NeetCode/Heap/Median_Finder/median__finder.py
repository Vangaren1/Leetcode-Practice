from typing import Optional, List

import heapq


class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        pass

    def addNum(self, num: int) -> None:
        if not self.minHeap and not self.maxHeap:
            heapq.heappush(self.minHeap, num)
            return

        if num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        while abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                tmp = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -tmp)
            else:
                tmp = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, tmp)

    def findMedian(self) -> float:
        if len(self.minHeap) > 0 and len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]


if __name__ == "__main__":
    sol = MedianFinder()
    for i in (5, 3, 7, 2):
        sol.addNum(i)
        print(sol.findMedian())
    print("Running Solution...")
