from typing import Optional
from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterPile = defaultdict(int)

        for m in magazine:
            letterPile[m] +=1        
        for r in ransomNote:
            letterPile[r] -=1
            if letterPile[r] < 0:
                return False
        return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    s = Solution()
    print(s.canConstruct(ransomNote, magazine))
    print("Running Solution...")
