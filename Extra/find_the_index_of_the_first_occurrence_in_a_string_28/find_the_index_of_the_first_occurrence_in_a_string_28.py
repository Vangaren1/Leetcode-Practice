from typing import Optional, List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ptr1 = -1
        ptr2 = len(needle)-1
        
        result = -1
        
        while ptr1 < len(haystack) and ptr2 < len(haystack):
            ptr1 += 1
            ptr2 += 1
            
            curr = haystack[ptr1:ptr2]
            if curr == needle:
                return ptr1

            
        return result

if __name__ == "__main__":
    haystack = "butsa"
    needle = "sad"
    
    s = Solution()
    
    print(s.strStr(haystack, needle))

    print("Running Solution...")
