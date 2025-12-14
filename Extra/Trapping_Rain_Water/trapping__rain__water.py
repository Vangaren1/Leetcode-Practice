from typing import Optional, List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n

        maxLeft[0] = height[0]
        maxRight[-1] = height[-1]

        for index in range(1, n):
            maxLeft[index] = max(height[index], maxLeft[index - 1])
            maxRight[-index - 1] = max(height[-index - 1], maxRight[-index])

        total = 0
        for index in range(n):
            tmp = min(maxLeft[index], maxRight[index]) - height[index]
            if tmp > 0:
                total += tmp
        return total


if __name__ == "__main__":
    sol = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    Output = 6
    assert sol.trap(height) == Output
    print("Running Solution...")
