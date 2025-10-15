from typing import Optional, List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        f = [0] * len(skill)

        mVal = 0


if __name__ == "__main__":
    sol = Solution()
    skill = [1, 5, 2, 4]
    mana = [5, 1, 4, 2]
    print(sol.minTime(skill, mana))
    print("Running Solution...")
