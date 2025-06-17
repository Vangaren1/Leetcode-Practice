from typing import Optional, List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palinCheck(index):
            ptr2 = ptr1 = ptr3 = index
            ptr4 = index + 1
            if ptr4 == len(s):
                return s[index]
            
            even = s[ptr3] == s[ptr4]
            odd = True
            
            currEven = ""
            currOdd = ""
            
            if even:
                currEven = s[ptr3:ptr4+1]
            else:
                currOdd = s[ptr2:ptr1+1]
            while even or odd:
                if odd:
                    if ptr2 < 0 or ptr1 == len(s):
                        break
                    odd = s[ptr2] == s[ptr1]
                    if not odd: 
                        continue
                    currOdd = s[ptr2:ptr1+1]
                    ptr2 -= 1
                    ptr1 += 1
                    
                if even:
                    if ptr3 < 0 or ptr4 == len(s):
                        break
                    even = s[ptr3] == s[ptr4]
                    if not even:
                        continue
                    currEven = s[ptr3:ptr4+1]
                    ptr3 -= 1
                    ptr4 += 1
            
            if len(currEven) > len(currOdd):
                return currEven
            return currOdd

        longest = ""
        
        for index in range(0,len(s)):
            tmp = palinCheck(index)
            if len(tmp) > len(longest):
                longest = tmp
        return longest

if __name__ == "__main__":
    sol = Solution()
    s = "ccc"
    
    print(sol.longestPalindrome(s))
    
    print("Running Solution...")
