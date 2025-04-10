class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        lastLen = len(nums)
        if lastLen == 1:
            return nums[0]
        while len(nums) > 0:
            last = nums.pop(0)
            if last in nums:
                nums.remove(last)
            else:
                return last
        pass


a = [2,2,1, 3,4,5]
last = a.pop(0)
if last in a:
    print("last still in list")
    a.remove(last)
else:
    print("last no longer in list")

print(a)

s = Solution()
test = [[2,2,1], [4,1,2,1,2], [1]]

for t in test:
    print(s.singleNumber(t))
