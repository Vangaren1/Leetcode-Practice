from typing import Optional, List


class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:

        count = 0
        n = len(damage)

        for starting in range(n):
            h = hp
            for room in range(starting, n):
                h -= damage[room]

                if h <= 0:
                    break

                if h >= requirement[room]:
                    count += 1

        return count

        pass


if __name__ == "__main__":
    sol = Solution()
    hp = 2
    damage = [10000, 1]
    requirement = [1, 1]

    print(sol.totalScore(hp, damage, requirement))
    print("Running Solution...")


"""You are given a positive integer hp and two positive 1-indexed integer arrays damage and requirement.

There is a dungeon with n trap rooms numbered from 1 to n. Entering room i reduces your health points by damage[i]. After that reduction, if your remaining health points are at least requirement[i], you earn 1 point for that room.©leetcode
        """
