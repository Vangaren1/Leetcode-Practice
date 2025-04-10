import string

class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        ptr = 0
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[ptr] in ['-','+']:
            if s[ptr] == '-':
                negative = True
            s = s[1:]
        if len(s) == 0:
            return 0
        if s[0] not in string.digits:
            return 0
        temp = ""
        while s[ptr].isnumeric():
            temp += s[ptr]
            ptr += 1
            if ptr > len(s) - 1:
                break
        num = temp
        exp = len(num)-1
        sum = 0
        for i in range(len(num)):
            d = string.digits.find(num[i])
            sum += d * 10 ** exp
            exp -= 1
        if negative:
            sum *= -1
        if sum < (-1 * 2**31):
            return (-1 * 2**31)
        if sum > (2**31 - 1):
            return 2**31 - 1
        return sum


obj = Solution()
print(obj.myAtoi("52"))
print(obj.myAtoi("4193 with words"))
print(obj.myAtoi("3.124159"))
print(obj.myAtoi("     52 with words"))
print(obj.myAtoi(" -04f"))
print(obj.myAtoi("+"))