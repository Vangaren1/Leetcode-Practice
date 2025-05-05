from typing import Optional, List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(interval1, interval2):
            # [0,2] and [1,3]
            onTheLeft = interval1[1] >= interval2[0] and interval1[0] <= interval2[0]
            # [1,3] and [2,4]
            onTheRight = interval1[0] <= interval2[1] and interval1[1] >= interval2[0]
            # [1,4] and [2,3]
            inTheMiddle = interval1[0] <= interval2[0] and interval1[1] >= interval2[1]
            if onTheLeft or onTheRight or inTheMiddle:
                left = min(interval1[0], interval2[0])
                right = max(interval1[1], interval2[1])
                return (True, [left,right])
            else:
                return (False, None)
        def inBetween(first, second, third):
            return first[1] < second[0] and second[1] < third[0]
        
        # empty interval list    
        if len(intervals) == 0:
            return [newInterval]
        # before the start of the interval list
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        # after the end of the list
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        first, second = newInterval
        overlapped = False
        for i in range(len(intervals)):
            check = overlap(intervals[i], newInterval)
            if check[0]:
                intervals[i] = check[1]
                overlapped = True
                break

        ptr = 0
        length = len(intervals)
        while(ptr < length -1):
            first = intervals[ptr]
            second = intervals[ptr+1]
            check = overlap(first, second)
            if check[0]:
                intervals[ptr] = check[1]
                intervals.pop(ptr+1)
            elif not overlapped and inBetween(first, newInterval, second):
                List.insert(intervals, ptr+1, newInterval)
                return intervals
            else:
                ptr += 1
            length = len(intervals)
        return intervals
        
            
            
            
            
        pass

if __name__ == "__main__":
    intervals = [[3,5],[12,15]]
    newInterval = [6,8]
    s = Solution()
    print(s.insert(intervals, newInterval))
    print("Running Solution...")
