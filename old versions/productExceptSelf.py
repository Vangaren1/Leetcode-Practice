import math

class Solution:
    def productExceptSelf(self, nums):
        pre, post = 1, 1
        length = len(nums)
        output = [ 1 for _ in range(length)]
        # first pass
        for i in range(length):
            output[i]=pre
            pre *= nums[i]
        # second pass
        for j in range(length, 0,-1):
            output[j-1] *= post
            post *= nums[j-1]
        return output







sol = Solution()

t1 = [1,2,3,4]        
s1 = [24,12,8,6]

t2 = [-1,1,0,-3,3]
s2 = [0,0,9,0,0]

print(sol.productExceptSelf(t1))
print(sol.productExceptSelf(t2))

