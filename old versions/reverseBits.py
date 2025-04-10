class Solution:
    def reverseBits(self, n: int) -> int:
        if len(str(n)) != 32:
            t = format(n, 'b')
        else:
            t = str(n)
        r = t[::-1]
        while len(r) < 32:
            r += '0'
        return int(r, 2)
        
        

obj = Solution()

test1 = 10100101000001111010011100
test2 = 11111111111111111111111111111101

print(format(test1, "b"))

