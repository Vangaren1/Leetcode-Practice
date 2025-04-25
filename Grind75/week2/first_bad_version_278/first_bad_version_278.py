from typing import Optional

def isBadVersion(version: int) -> bool:
    return version >= 1

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        mid = (start + end ) // 2
        while True:
            check = isBadVersion(mid)
            if not check:
                start = mid + 1
            else:
                end = mid
                if not isBadVersion(mid - 1):
                    return mid 
            mid = (start + end) // 2 

    


if __name__ == "__main__":
    
    n = 5
    s = Solution()
    
    print(s.firstBadVersion(n))
    
    print("Running Solution...")
