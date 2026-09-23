from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        height = len(matrix)
        width = len(matrix[0])
        maxArea = 0
        dp = [[0 for _ in range(width)] for _ in range(height + 1)]

        for y in range(height):
            for x in range(width):
                if matrix[y][x] == "1":
                    dp[y + 1][x] = 1 + dp[y][x]

        for row in dp:
            maxArea = max(maxArea, self.largestRectangleArea(row))
        return maxArea

        pass

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
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "1", "1", "0"],
    ]
    print(sol.maximalRectangle(matrix))
    print("Running Solution...")
