import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        test1 = math.log2(n)
        test2 = 2 ** int(test1)
        return test2 == n 

obj = Solution()


for i in range(1,33):
    print("i: %d, result: %s" % (i, str(obj.isPowerOfTwo(i))))