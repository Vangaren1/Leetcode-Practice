from typing import Optional, List
from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sDict = defaultdict(int)
        for ch in s:
            sDict[ch] += 1
        tDict = defaultdict(int)
        for ch in t:
            tDict[ch] += 1
            
        for key, value in tDict.items():
            if tDict[key] != sDict[key]:
                return key
        

if __name__ == "__main__":
    s = Solution()
    s = "abcd"
    t = "abcde"
    print("Running Solution...")
