from typing import Optional, List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                maxArea = max(maxArea, h * (index - idx))
                start = idx

            stack.append((start, height))

        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea


if __name__ == "__main__":
    sol = Solution()
    heights = [7, 1, 7, 2, 2, 4]

    print(sol.largestRectangleArea(heights))
    print("Running Solution...")
