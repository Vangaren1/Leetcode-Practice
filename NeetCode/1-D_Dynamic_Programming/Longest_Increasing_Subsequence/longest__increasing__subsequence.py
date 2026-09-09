from typing import Optional, List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        tails = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(sol.lengthOfLIS(nums))
    print("Running Solution...")

# This is too memory heavy
# def lengthOfLIS(self, nums: List[int]) -> int:
#     seq = []

#     for num in nums:
#         check = [n for n in seq if n[-1] < num]
#         if len(check) == 0:
#             seq.append([num])
#             continue
#         for c in check:
#             if num > c[-1] + 1:
#                 seq.append(c.copy())
#             c.append(num)

#     return max([len(s) for s in seq])
