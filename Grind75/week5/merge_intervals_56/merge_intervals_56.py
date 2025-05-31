from typing import Optional, List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(a: List[int], b: List[int]):
            if a[1] > b[0] or a[1] > b[1] or a[0] > b[1] or a[0] > b[0]:
                return True
            return False
        
        intervals.sort()
        ptrA = 0
        length = len(intervals)
        
        while ptrA < length-1:
            if overlap(intervals[ptrA], intervals[ptrA+1] ):
                intervals[ptrA][0] = min(intervals[ptrA][0], intervals[ptrA+1][0])
                intervals[ptrA][1] = max(intervals[ptrA][1], intervals[ptrA+1][1])
                intervals.pop(ptrA+1)
                length = len(intervals)
            else:
                ptrA += 1
        
        return intervals


if __name__ == "__main__":
    intervals = [[1,4],[0,0]]
    s = Solution()
    
    print(s.merge(intervals))
    print("Running Solution...")
