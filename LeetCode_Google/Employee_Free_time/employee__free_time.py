from typing import Optional, List
import heapq
from collections import defaultdict

"""
# Definition for an Interval.
"""


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        initial = Interval(float("-inf"), float("inf"))
        freeTime = [initial]
        # takes a single interval b, and if it overlaps with a, breaks it in two intervals that do not overlap with b

        def divide(a, b):
            # no overlap
            if b.end <= a.start or b.start >= a.end:
                return [a]

            # b completely covers a
            if b.start <= a.start and b.end >= a.end:
                return []

            # b cuts off left side
            if b.start <= a.start:
                return [Interval(b.end, a.end)]

            # b cuts off right side
            if b.end >= a.end:
                return [Interval(a.start, b.start)]

            # b is completely inside a
            return [Interval(a.start, b.start), Interval(b.end, a.end)]

        for employee in schedule:
            for shift in employee:
                newFree = []
                for inter in freeTime:
                    tmp = divide(inter, shift)
                    for t in tmp:
                        newFree.append(t)
                freeTime = newFree

        results = []
        for f in freeTime:
            if f.start != float("-inf") and f.end != float("inf"):
                results.append(f)
        return results


if __name__ == "__main__":
    sol = Solution()
    schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    sch = []
    for employee in schedule:
        tmp = []
        for shift in employee:
            tmp.append(Interval(shift[0], shift[1]))
        sch.append(tmp)
    print(sol.employeeFreeTime(sch))
    print("Running Solution...")
