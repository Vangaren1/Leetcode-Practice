from typing import Optional, List
import string

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) <= 0:
            return 0
        ptr = 0
        digits = string.digits

        sign = 1
        curr = s[0]
        if curr not in digits and curr not in ['+', '-']:
            return 0
        elif curr in ['+', '-']:
            ptr += 1
            sign = -1 if curr == '-' else 1
        if ptr == len(s):
            return 0

        # skip over '0's
        total = 0
        curr = s[ptr]
        while ptr < len(s) -1 and curr == '0':
            ptr += 1
            curr = s[ptr]
        if ptr == len(s):
            return 0
        
        while curr in digits and ptr < len(s) :
            curr = s[ptr]
            if curr in digits:
                total = total * 10 + (ord(curr)-48)
            else:
                break
            ptr += 1
            
        
        total *= sign    
        MINVAL = -(2**31)
        MAXVAL = 2**31 - 1

        total = max(total, MINVAL)
        total = min(total, MAXVAL)
                
        return total    
         
        
        pass

if __name__ == "__main__":
    s = Solution()
    st = "21474836460"
    testCases = [
        "    0000000000000   ",
        "42",
        "   -042",
        "1337c0d3",
        "0-1",
        "words and 987",
        "",
        "+",
        "21474836460"
    ]
    expected = [
        0,
        42, 
        -42,
        1337,
        0,
        0,
        0,
        0,
        2147483647
    ]
    for index in range(len(testCases)):
        print(s.myAtoi(testCases[index]))
        print("expected {}".format(expected[index]))
        
    print(s.myAtoi(st))
    print("Running Solution...")
