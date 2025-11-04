from typing import Optional, List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        pathgrid = [[0] * width for _ in range(height)]
        for row in pathgrid:
            row.append(float("inf"))
            row.insert(0, float("inf"))
        pathgrid.insert(0, [float("inf") for _ in range(width + 2)])
        pathgrid.append([float("inf") for _ in range(width + 2)])

        maxDepth = grid[height-1][width-1]
        steps = 0
        for y in range(height, 0,-1):
            for x in range(width, 0, -1):
                # check the distances around y,x and see
                # if the distance to reach it is less than maxDepth
                minDepth = min( pathgrid[y+1][x], pathgrid[y-1][x], pathgrid[y][x+1], pathgrid[y][x-1])
                # record steps to reach this level
                if grid[y-1][x-1] >= maxDepth:
                    step +=1 
                    pathgrid[y][x] = step
                
                
        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [0, 2],
        [1, 3],
    ]
    print(sol.swimInWater(grid))
    print("Running Solution...")
