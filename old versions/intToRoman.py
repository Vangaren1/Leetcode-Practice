class Solution:
    int2ro = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
    def intToRoman(self, num):
        if num in self.int2ro.keys():
            return self.int2ro[num]
        if num > 1000:
            return 'M'+self.intToRoman(num-1000)
        if num < 1000 and num >= 900:
            return 'CM'+self.intToRoman(num-900)
        if num > 500:
            return 'D'+self.intToRoman(num-500)
        if num < 500 and num >= 400:
            return 'CD'+self.intToRoman(num-400)
        if num > 100:
            return 'C'+self.intToRoman(num-100)
        if num < 100 and num >= 90:
            return 'XC'+self.intToRoman(num-90)
        if num > 50:
            return 'L'+self.intToRoman(num-50)
        if num < 50 and num >= 40:
            return 'XL'+self.intToRoman(num-400)   
        if num > 10:
            return 'D'+self.intToRoman(num-10)
        if num == 9:
            return 'IX'
        if num > 5: 
            return 'V'+self.intToRoman(num-5)
        if num == 4:
            return 'IV'
        if num > 0:
            return 'I'+self.intToRoman(num-1)
        return ''

        

sol = Solution()

print(sol.intToRoman(123))
print("III" == sol.intToRoman(3))