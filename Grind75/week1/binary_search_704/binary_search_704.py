from typing import Optional, List 


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = end // 2
        last = -1
        while nums[mid] != target:
            if mid == last: 
                return -1
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            last = mid
            mid = (start + end) // 2             
        return mid
    

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 2
    expected = -1
    s = Solution()
    assert s.search(nums, target) == expected
    print("Running Solution...")
