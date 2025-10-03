from typing import Optional, List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for index in range(len(intervals) - 1):
            if intervals[index].end > intervals[index + 1].start:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    intervals = [(0, 30), (5, 10), (15, 20)]
    print(sol.canAttendMeetings(intervals))
    print("Running Solution...")
