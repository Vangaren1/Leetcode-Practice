from typing import Optional, List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        colSets = []
        for _ in range(len(grid[0])):
            colSets.append(set())

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                curr = grid[y][x]
                colSets[x].add(curr)
                if len(colSets[x]) > 1:
                    return False

        last = None
        colSets = [list(i)[0] for i in colSets]
        for col in colSets:
            if col == last:
                return False
            last = col
        return True


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 1, 1], [0, 0, 0]]
    print(sol.satisfiesConditions(grid))
    print("Running Solution...")
