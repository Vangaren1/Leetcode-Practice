from typing import Optional


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def addAB(a, b, c):
            return ((a ^ b) ^ c, (a and b) or (c & (a ^ b)))
        result = ""
        carry = 0
        a = [ int(i) for i in a]
        b = [ int(i) for i in b]
        while a and b:
            abit = a.pop(-1)
            bbit = b.pop(-1)
            sum, carry = addAB(abit, bbit, carry)
            result = "{}".format(sum) + result
        while a:
            abit = a.pop(-1)
            sum, carry = addAB(abit, carry, 0)
            result = "{}".format(sum)  + result
        while b: 
            bbit = b.pop(-1)
            sum, carry = addAB(bbit, carry, 0)
            result = "{}".format(sum)  + result
        if carry == 1:
            result = "1" + result
        return result
    
if __name__ == "__main__":
    s = Solution()
    a = "110010"
    b = "10111"
    print(s.addBinary(a,b))
    print("Running Solution...")
