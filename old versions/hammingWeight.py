class Solution:
    def hammingWeight(self, n) -> int:
        t = str(n)
        sum = 0
        for d in t:
            if d == '1':
                sum +=1 
        return sum

test = 1011

obj = Solution()
print(obj.hammingWeight(1011))