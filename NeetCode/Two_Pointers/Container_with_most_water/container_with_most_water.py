from typing import Optional, List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        mArea = 0
        mLeft, mRight = 0, 0

        while left < right:
            mLeft = max(mLeft, heights[left])
            mRight = max(mRight, heights[right])
            volume = min(mLeft, mRight) * (right - left)
            mArea = max(mArea, volume)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return mArea


if __name__ == "__main__":
    sol = Solution()
    height = [1, 7, 2, 5, 4, 7, 3, 6]

    print(sol.maxArea(height))
    print("Running Solution...")
