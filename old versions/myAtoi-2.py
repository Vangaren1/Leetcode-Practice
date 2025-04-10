import string

class Solution:
    def myAtoi(self, s: str) -> int:
    	s = s.strip()
    	if len(s) == 0: return 0
    	temp= ""
    	neg = False
    	if s[0] in ['-','+']:
    		if s[0] == '-':
    			neg = True
    		s = s[1:]
    	if len(s) == 0: return 0
    	while s[0].isdigit():
    		temp += s[0]
    		s = s[1:]
    		if len(s) == 0:
    			break
    	temp = temp[::-1]
    	exp = 0
    	sum = 0
    	for d in temp:
    		sum += string.digits.find(d) * (10 ** exp)
    		exp += 1
    	if neg:
    		sum = -sum
    	if sum < -(2**31): sum = -(2**31)
    	if sum > (2**31) - 1: sum = 2**31 - 1
    	return sum

    	

obj = Solution()
print(obj.myAtoi("52"))
print(obj.myAtoi("4193 with words"))
print(obj.myAtoi("3.124159"))
print(obj.myAtoi("     52 with words"))
print(obj.myAtoi(" -04f"))
print(obj.myAtoi("+"))