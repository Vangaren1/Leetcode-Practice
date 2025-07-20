from typing import Optional, List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1, ptr2 = 0, 0
        
        while ptr1 < len(s) and ptr2 < len(t):
            currS = s[ptr1]
            currT = t[ptr2]
            if currS == currT:
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
        
        return ptr1 >= len(s)

if __name__ == "__main__":
    sol = Solution()
    s = "abce"
    t = "ahbgdc"
    print(sol.isSubsequence(s,t))
    print("Running Solution...")
