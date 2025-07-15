from typing import Optional, List

import string

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = 'aeiouAEIOU'
        validCharacters = string.ascii_letters + string.digits
        sawVowel = False
        sawConsonant = False 
        for ch in word:
            if ch not in validCharacters:
                return False
            if ch in vowels:
                sawVowel = True
            if ch not in vowels and ch not in string.digits:
                sawConsonant = True
            
        return sawVowel and sawConsonant
                
            
        
        pass

if __name__ == "__main__":
    print("Running Solution...")
