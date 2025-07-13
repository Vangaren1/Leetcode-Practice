from typing import Optional, List
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def valid(a, b):
            for key in b.keys():
                if a.get(key, 0) < b.get(key):
                    return False
            return True
        
        if len(t) > len(s):
            return ""
        
        tDict = dict(Counter(t))
        currDict = defaultdict(int)
        ptr1, ptr2 = 0, 0
        currMin = ""
        minLen = float('inf')
        
        while ptr2 < len(s):
            # move ptr2 until it's a valid substring
            curr = s[ptr2]
            if curr in tDict.keys():
                currDict[curr] += 1
            ptr2 += 1
            
            # move ptr1 right until it's the minimum valid string
            while valid(currDict, tDict):
                if ptr2 - ptr1 < minLen:
                    minLen = ptr2 - ptr1
                    currMin = s[ptr1:ptr2]
                    
                curr = s[ptr1]
                if curr in currDict:
                    currDict[curr] -= 1
                ptr1 += 1
                    
            
        return currMin
        


        
        
        
if __name__ == "__main__":
    sol = Solution()
    
    s = "ADOBECODEBANC"
    t = "ABC"
    expected = "BANC"
    
    assert sol.minWindow(s,t) == expected
    
    s = "A"
    t = "AA"
    
    assert sol.minWindow(s,t) == ""
    
    s = "A"
    t = "A"
    
    assert sol.minWindow(s,t) == "A"
    
    s = "A"
    t = "B"
    
    assert sol.minWindow(s,t) == ""
    
    s = "AB"
    t = "A"
    
    assert sol.minWindow(s,t) == "A"
    
    s = "ABC"
    t = "A"
    assert sol.minWindow(s,t) == "A"
    
    
    print(sol.minWindow(s,t))
    
    print("Running Solution...")
