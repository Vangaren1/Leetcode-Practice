from typing import Optional, List

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        firstPos = {}
        
        for index in range(len(s)):
            curr = s[index]
            count[curr] += 1
            if curr not in firstPos:
                firstPos[curr] = index
            
        single = [ ch for ch in count.keys() if count[ch] == 1 ]
        ind = [ firstPos[ch] for ch in single ]
        ind.sort()
        return ind[0]

if __name__ == "__main__":
    s = Solution()
    st = "loveleetcode"
    print(s.firstUniqChar(st))
    print("Running Solution...")
