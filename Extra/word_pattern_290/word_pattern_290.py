from typing import Optional, List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False

        sDict = {}
        
        for index in range(len(pattern)):
            currP = pattern[index]
            currS = s[index]
            if currP in sDict:
                if sDict[currP] != currS:
                    return False
            else:
                if currS in sDict.values():
                    return False
                sDict[currP] = currS 
        return True
                            
        
        
        
        pass

if __name__ == "__main__":
    
    pattern = "abba"
    s = "dog cat cat dog"
    sol = Solution()
    
    print(sol.wordPattern(pattern, s))
    print("Running Solution...")
