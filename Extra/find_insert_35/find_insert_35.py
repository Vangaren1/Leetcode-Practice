from typing import Optional, List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(nums, target):
            left = 0
            right = len(nums) - 1
            mid = (left + right) // 2
            
            while left < right:
                curr = nums[mid]
                if curr == target:
                    return mid
                elif curr < target:
                    left = mid + 1
                else: 
                    if mid == 0:
                        return 0
                    right = mid -1
                mid = (left + right) // 2
            return mid

        find = search(nums, target)
        if nums[find] < target:
            return find + 1
        return find 
    

if __name__ == "__main__":
    s = Solution()
    
    nums = [1,3]
    target = 0
    
    print(s.searchInsert(nums, target))
    print("Running Solution...")
