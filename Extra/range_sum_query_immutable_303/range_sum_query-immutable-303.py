from typing import Optional, List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [1]*len(nums)
        self.sums[0] = self.nums[0]
        for index in range(1,len(nums)):
            self.sums[index] = self.nums[index] + self.sums[index-1]
        print(self.sums)
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        
        return self.sums[right] - self.sums[left-1]


if __name__ == "__main__":
    n = NumArray([-2,0,3,-5,2,-1])
    
    print(n.sumRange(2,5))
    print("Running Solution...")
