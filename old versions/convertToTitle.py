import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        cnum = columnNumber - 1
        if cnum <= 25:
            return string.ascii_uppercase[cnum]
        temp = cnum % 26
        return self.convertToTitle( (cnum - temp) // 26)  + string.ascii_uppercase[temp]



# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         up = string.ascii_uppercase
#         rstr = ''
#         cnum = columnNumber
#         if cnum <= 26 and 0 < cnum:
#             return up[cnum - 1]
#         rstr = up[(cnum % 26 ) - 1 ]
#         cnum -= (cnum % 26)
#         cnum = cnum // 26
#         while cnum != 0:
#             r = cnum % 26
#             rstr = up[r - 1 ] + rstr
#             cnum = int( (cnum - r) / 26)

#         return rstr


obj = Solution()
print(obj.convertToTitle(701))
print(obj.convertToTitle(1))
print(obj.convertToTitle(28))
print(obj.convertToTitle(28))

