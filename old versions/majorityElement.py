class Solution:
    def majorityElement(self, nums) -> int:
        count = {}
        length = len(nums)
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        return max(count, key = count.get)

        







obj = Solution()
results = obj.majorityElement([3,2,3])
assert results == 3, "Failed first test"


obj = Solution()
results = obj.majorityElement([2,2,1,1,1,2,2])
assert results == 2, "Failed second test"