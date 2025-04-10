class Solution:
    def twoSum(self, nums, target):
        first = 0
        second = 1
        m = len(nums)
        while True:
            if nums[first]+nums[second]==target:
                return [first, second]
            else:
                second += 1
                if second == m:
                    first += 1 
                    second = first + 1


s = Solution()

print(s.twoSum([2,7,11,13], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))

        