from typing import Optional, List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        nums.insert(0, 1)
        nums.append(1)

        fromLeft = [1] * len(nums)
        fromRight = [1] * len(nums)

        for index in range(1, len(nums)):
            fromLeft[index] = nums[index - 1] * fromLeft[index - 1]
            fromRight[-index - 1] = nums[-index] * fromRight[-index]

        results = [fromLeft[i] * fromRight[i] for i in range(1, len(nums) - 1)]
        return results


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    print(sol.productExceptSelf(nums))

    nums = [-1, 1, 0, -3, 3]
    print(sol.productExceptSelf(nums))
    print("Running Solution...")
