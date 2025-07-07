from typing import Optional, List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        count = 0
        while ptr < len(nums):
            if nums[ptr] == 0:
                nums.pop(ptr)
                count += 1
            else:
                ptr += 1
        
        while count > 0:
            nums.append(0)
            count -= 1

if __name__ == "__main__":
    print("Running Solution...")
