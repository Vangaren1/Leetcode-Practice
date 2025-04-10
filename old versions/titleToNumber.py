import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        e = len(columnTitle) - 1
        for c in columnTitle:
            i = string.ascii_uppercase.index(c) + 1 
            sum += i * (26**e)
            e -= 1 
        return sum

obj = Solution()

print(obj.titleToNumber('AA'))
print(obj.titleToNumber('AB'))

