from typing import Optional, List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        results = []
        
        #if you can't make an anagram of p from s
        if len(p) > len(s):
            return results
        
        pDict = defaultdict(int)
        for ch in p:
            pDict[ch] += 1
        
        ptr1 = 0
        ptr2 = 0
        
        buffer = defaultdict(int)
        
        while ptr2 < len(p):
            buffer[s[ptr2]] += 1
            ptr2 += 1
        
        
        while ptr1 <= len(s) and ptr2 <= len(s):

            anaCheck = dict(buffer) == dict(pDict)
            # if they're the same, record ptr1 in results and continue
            if anaCheck: 
                results.append(ptr1)

            if ptr1 == len(s) or ptr2 == len(s):
                break

            buffer[s[ptr1]] -= 1
            if buffer[s[ptr1]] == 0:
                buffer.pop(s[ptr1])
            buffer[s[ptr2]] += 1
            
            ptr1 += 1            
            ptr2 += 1

        
        return results

if __name__ == "__main__":
    sol = Solution()
    
    s = "abab"
    p = "ab"
    print(sol.findAnagrams(s,p))
    print("Running Solution...")
