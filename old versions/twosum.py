from itertools import combinations

nums_example = [2,1,8,11,15]


def twoSum(nums, target):
	def getPair():
		length = len(nums)
		comb = combinations(nums,2)
		for c in comb:
			if c[0]+c[1]==target:
				return c
	pair = getPair()
	if pair is not None:
		if pair[0]==pair[1]:
			first = nums.index(pair[0])
			for i in range(first+1,len(nums)):
				if nums[i]==pair[1]:
					return [first,i]
		else:
			return [nums.index(pair[0]), nums.index(pair[1])]
		

print(twoSum(nums_example,9))
print(twoSum([3,3],6))
