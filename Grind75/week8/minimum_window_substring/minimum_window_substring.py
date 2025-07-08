from typing import Optional, List
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def validSub(a: dict, b: dict):
            #returns true if all the items in a are in b
            if len(a.keys()) < len(b.keys()):
                return False
            for key in b.keys():
                if b.get(key) > a.get(key, 0):
                    return False
            return True
            
        req = dict(Counter(t))
        
        curr = defaultdict(int)
        
        ptr1 = 0
        # find start of substring
        while s[ptr1] not in req.keys():
            ptr1 += 1
        
        ptr2 = ptr1
        # find the first string that contains a valid substring
        while ptr2 < len(s) and not validSub(curr, req):
            if s[ptr2] in req.keys():
                curr[s[ptr2]] += 1
            ptr2 += 1
        
        # if the end of the array is reached and no valid substring is found, return """
        if not validSub(curr, req):
            return ""
        
        currMin = s[ptr1:ptr2]
        
        while ptr1 < len(s) and ptr2 < len(s):
            # remove the first 
            curr[s[ptr1]] -= 1
            ptr2 += 1
            # advance ptr2 until the substring is valid again
            while ptr2 < len(s) and not validSub(curr, req):
                if s[ptr2] in req.keys():
                    curr[s[ptr2]] += 1
                ptr2 += 1
            
            ptr1 += 1
            #advance ptr1 till it reaches a character in t
            while s[ptr1] not in t:
                ptr1 += 1
                
            
            # check if it's valid, if it is, compare to currMin
            if validSub(curr, req) and (ptr2-ptr1 < len(currMin)):
                currMin[ptr1:ptr2]
                
        return currMin
        
        
        
        
if __name__ == "__main__":
    sol = Solution()
    
    s = "ADOBECODEBANC"
    t = "ABC"
    expected = "BANC"
    
    print(sol.minWindow(s,t))
    
    print("Running Solution...")
