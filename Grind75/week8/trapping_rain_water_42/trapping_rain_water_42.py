from typing import Optional, List


class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l = len(height)
        maxRight = [
            0,
        ] * l
        maxLeft = [
            0,
        ] * l
        minLR = [
            0,
        ] * l

        for i in range(1, l):
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1])
            maxRight[l - i - 1] = max(height[l - i], maxRight[l - i])

        for j in range(l):
            minLR[j] = min(maxLeft[j], maxRight[j])
            tmp = minLR[j] - height[j]
            if tmp > 0:
                total += tmp

        return total


if __name__ == "__main__":
    s = Solution()

    heights = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([4, 2, 3], 1),
    ]
    print(s.trap(heights[0][0]))
    # for h in heights:
    #     result = s.trap(h[0])
    #     assert s.trap(h[0]) == h[1]
    print("Running Solution...")
