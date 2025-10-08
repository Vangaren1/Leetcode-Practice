from typing import Optional, List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        startTimes = [i.start for i in intervals]
        endTimes = [e.end for e in intervals]
        startTimes.sort()
        endTimes.sort()

        sPtr, ePtr, count, maxCount = 0, 0, 0, 0
        size = len(intervals)

        while sPtr < size and ePtr < size:
            if startTimes[sPtr] < endTimes[ePtr]:
                sPtr += 1
                count += 1
            else:
                ePtr += 1
                count -= 1
            maxCount = max(maxCount, count)
        return maxCount


if __name__ == "__main__":
    sol = Solution()
    intervals = [(0, 40), (5, 10), (15, 20)]
    intervals = [Interval(i[0], i[1]) for i in intervals]
    print(sol.minMeetingRooms(intervals))

    print("Running Solution...")
