from typing import Optional, List


from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorCount = defaultdict(int)
        for n in nums:
            colorCount[n] += 1
        k = list(colorCount.keys())
        k.sort()
        
        for i in range(len(nums)):
            nums[i] = k[0]
            colorCount[k[0]] -= 1
            if colorCount[k[0]] == 0:
                k.pop(0)
    

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    s = Solution()
    s.sortColors(nums)
    print(nums)
    print("Running Solution...")
