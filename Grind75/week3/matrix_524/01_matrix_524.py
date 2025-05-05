from typing import Optional, List
import string

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        queue = []
        for x in range(len(mat[0])):
            for y in range(len(mat)):
                if mat[y][x] != 0:
                    mat[y][x] = '?'
                else:
                    queue.append((y,x))
                    
        def bfs():
            nonlocal queue
            diff = [(1,0), (-1,0), (0,1), (0,-1)]
            while queue:
                y,x = queue.pop(0)
                for dy, dx in diff:
                    ny = y + dy 
                    nx = x + dx
                    if 0 <= ny < height and 0 <= nx < width: 
                        if mat[ny][nx] == '?':
                            mat[ny][nx] = mat[y][x] + 1
                            queue.append((ny,nx))
                        else:
                            mat[ny][nx] = min(mat[ny][nx], mat[y][x] + 1)
        bfs()
        return mat
                    
                    
                            
                            

if __name__ == "__main__":
    mat = [[0],[0],[0],[0],[0]]
    s = Solution()
    s.updateMatrix(mat)
    print("Running Solution...")
