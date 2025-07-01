from typing import Optional, List

import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = string.ascii_uppercase
        tmp = ''
        while columnNumber > 0:
            columnNumber -= 1
            digit = columnNumber % 26
            tmp = letters[ digit ] + tmp
            
            columnNumber = ( columnNumber ) // 26
            
        return tmp

if __name__ == "__main__":
    s = Solution()
    
    print()
    print(s.convertToTitle(28))
    print(s.convertToTitle(701))
    # for i in range(1,40):
    #     print(s.convertToTitle(i))
    print("Running Solution...")
