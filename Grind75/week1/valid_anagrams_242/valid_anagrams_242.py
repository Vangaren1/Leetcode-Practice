from typing import Optional

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        
        for c in s:
            sDict[c] += 1
        for c in t:
            tDict[c] += 1
            
        return sDict == tDict
    

if __name__ == "__main__":
    print("Running Solution...")
