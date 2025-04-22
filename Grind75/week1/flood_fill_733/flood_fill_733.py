from typing import Optional, List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        adj = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = [(sr,sc)]
        changed = set()
        while queue:
            row,col = queue.pop(0)
            image[row][col] = color
            changed.add((row,col))
            for dy,dx in adj:
                newY, newX = row + dy, col + dx
                if 0 <= newY < len(image) and 0 <= newX < len(image[0]) and image[newY][newX] == original:
                    n = (newY, newX)
                    if n not in queue and n not in changed:
                        queue.append(n)
        return image

if __name__ == "__main__":
    s = Solution()
    image = [[0,0,0], [0,0,0]]
    sr = 0
    sc = 0
    color = 0
    Output= [[2,2,2],[2,2,0],[2,0,1]]
    
    s.floodFill(image, sr, sc, color)
    
    print("Running Solution...")
