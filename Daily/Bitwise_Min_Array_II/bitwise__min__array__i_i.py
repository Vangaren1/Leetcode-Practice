from typing import Optional, List

"""_summary_
i        dec(i)        ->   dec(ans)   ans
2   ->   10            ->     -1
3   ->   11            ->     1   (1)
5   ->   101           ->     4   (100)
7   ->   111           ->     3   (11)
11  ->   1011          ->     9   (1001)
13  ->   1101          ->     12  (1100)
17  ->   10001         ->     16  (10000)
19  ->   10011         ->     17  (10001)
23  ->   10111         ->     19  (10011)
29  ->   11101         ->     28  (11100)
31  ->   11111         ->     15  (1111)
---
    """


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num <= 2:
                tmp = -1
            else:
                t = (num ^ (num + 1)).bit_length() - 1
                tmp = num - 2 ** (t - 1)

            ans.append(tmp)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 5, 7]
    print(sol.minBitwiseArray(nums))
    print("Running Solution...")
