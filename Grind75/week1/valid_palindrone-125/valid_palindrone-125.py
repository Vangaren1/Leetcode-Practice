from typing import Optional


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ c.lower() for c in s if c.isalnum() ]
        head = 0
        tail = len(s) -1
        while head < tail:
            if s[head] != s[tail]:
                return False
            head += 1
            tail -= 1
        return True
    
    
if __name__ == "__main__":
    t1 =  "A man, a plan, a canal: Panama"
    t2 =  "race a car"
    s = Solution()
    
    assert s.isPalindrome(t1) == True
    assert s.isPalindrome(t2) == False
    
    print("Running Solution...")
