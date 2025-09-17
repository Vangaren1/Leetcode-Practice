from typing import Optional, List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        goal = total // 2
        memo = set()
        memo.add(0)

        for index in range(len(nums) - 1, -1, -1):
            curr = nums[index]
            for m in memo.copy():
                tmp = curr + m
                if tmp <= goal:
                    memo.add(curr + m)
            if goal in memo:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [
        41,
        20,
        99,
        98,
        50,
        48,
        64,
        15,
        74,
        94,
        60,
        33,
        61,
        34,
        47,
        35,
        24,
        58,
        28,
        73,
        36,
        51,
        80,
        57,
        42,
        52,
        73,
        27,
        94,
        59,
        50,
        99,
        32,
        65,
        76,
        62,
        69,
        80,
        41,
        51,
        49,
        74,
        93,
        12,
        77,
        30,
        25,
        59,
        55,
        13,
        41,
        23,
        34,
        31,
        47,
        53,
        8,
        88,
        86,
        88,
        36,
        32,
        23,
        37,
        1,
        7,
        67,
        49,
        20,
        31,
        59,
        99,
        15,
        21,
        47,
        35,
        93,
        1,
        14,
        56,
        57,
        36,
        13,
        27,
        26,
        64,
        63,
        52,
        98,
        20,
        52,
        23,
        84,
        39,
        34,
        59,
        98,
        71,
        90,
        99,
    ]
    print(sol.canPartition(nums))
    print("Running Solution...")
