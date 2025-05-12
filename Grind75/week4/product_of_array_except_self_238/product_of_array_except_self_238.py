from typing import Optional, List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        
        zCount = 0
        for i in range(length):
            if nums[i] == 0:
                zCount += 1
            if zCount > 1:
                return [0] * length
        
        tmp = 1
        for i in range(length):
            result[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for j in range(length-1, -1, -1):
            result[j] *= tmp
            tmp *= nums[j]
        return result
        

if __name__ == "__main__":
    s=Solution()
    nums =[-1,1,0,-3,3]
    print(s.productExceptSelf(nums))
    print("Running Solution...")


