from typing import Optional, List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = length -1
        
        mid = (left + right) // 2
        
        while nums[mid] != target and left < right:
            last = (left, mid, right)
            # if the pivot is between left and mid and target isn't
            if nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            mid = (left + right) // 2
            if (left, mid, right) == last:
                return -1
            if left == right:
                return left if nums[left] == target else -1
        return mid if nums[mid] == target else -1
                


if __name__ == "__main__":
    nums = [3,1]
    target = 1
    s = Solution()
    print(s.search(nums, target))
    # for n in nums:
    #     print(s.search(nums, n))
    print("Running Solution...")
