from typing import Optional, List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        x=0
        y=0
        incX = True
        height = len(matrix)
        width = len(matrix[0])
        
        direction = ((1,0), (0, 1), (-1,0), (0,-1))
        dirPos = 0
        
        
        remaining = width * height
        results = []
        while remaining > 0:
            coord = (x,y)
            seen.add(coord)
            results.append(matrix[y][x])
            remaining -= 1
            
            dx, dy = direction[dirPos]
            x += dx
            y += dy
            
            if (x,y) in seen or y == height or y < 0 or x < 0 or x == width:
                x -= dx
                y -= dy
                dirPos += 1
                dirPos %= 4
                dx, dy = direction[dirPos]
                x += dx
                y += dy
        return results

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    print(s.spiralOrder(matrix))
    print("Running Solution...")
