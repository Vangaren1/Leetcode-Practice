from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        results = set()
        n = len(tiles)
        used = [False for _ in range(n)]
        tiles = "".join(sorted([ch for ch in tiles]))

        def dfs(curr):
            results.add(curr[:])
            if len(curr) >= n:
                return

            for index, ch in enumerate(tiles):
                if used[index]:
                    continue
                if (
                    index > 0
                    and tiles[index] == tiles[index - 1]
                    and not used[index - 1]
                ):
                    continue

                used[index] = True
                curr += ch

                dfs(curr)
                curr = curr[:-1]
                used[index] = False

        dfs("")
        results.remove("")

        return len(results)


if __name__ == "__main__":
    sol = Solution()
    print(sol.numTilePossibilities("AAABBC"))
    print("Running Solution...")
