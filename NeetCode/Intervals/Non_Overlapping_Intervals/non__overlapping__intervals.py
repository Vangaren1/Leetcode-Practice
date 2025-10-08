from typing import Optional, List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[0])

        prevEnd = intervals[0][1]

        res = 0

        for start, end in intervals[1:]:

            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)

        return res

        pass


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
