from typing import Optional, List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def flip(n):
            return int(bin(n)[2:][::-1])

        r = [(flip(n), n) for n in nums]
        r.sort()

        return [n[1] for n in r]

        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 4]
    print(sol.sortByReflection(nums))
    print("Running Solution...")
