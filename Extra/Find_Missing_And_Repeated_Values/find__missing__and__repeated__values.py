from typing import Optional, List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        repeated = -1
        seen = set()

        n = len(grid)
        r = set(range(1, n * n + 1))
        for row in grid:
            for n in row:
                if n in seen:
                    repeated = n
                if n in r:
                    r.remove(n)
                seen.add(n)
        result = [i for i in r]
        result.insert(0, repeated)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
