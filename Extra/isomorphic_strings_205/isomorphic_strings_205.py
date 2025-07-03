from typing import Optional, List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = {}
        sCount = 0
        tDict = {}
        tCount = 0
        for index in range(len(s)):
            
            if s[index] not in sDict:
                sDict[s[index]] = sCount
                sCount += 1
                
            if t[index] not in tDict: 
                tDict[t[index]] = tCount
                tCount += 1
                
            if sDict[s[index]] != tDict[t[index]]:
                return False 
            
        return True
            
        
if __name__ == "__main__":
    
    s = "foo"
    t = "bar"
    
    sol = Solution()
    
    assert sol.isIsomorphic(s,t) == False

    print("Running Solution...")
