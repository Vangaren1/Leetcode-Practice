from typing import Optional, List

from common.graphnode import GraphNode as Node, print_graph_bfs, build_graph
from collections import defaultdict


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        startLetter = defaultdict(list)
        
        height = len(board)
        width = len(board[0])
        
        for y in range(height):
            for x in range(width):
                startLetter[board[y][x]].append((y,x))
        
        seen = set()
        
        def bfs(letters, pos):
            if len(letters) == 0:
                return True
            dir = ((0,1),(0,-1),(1,0),(-1,0))
            found = []
            for dy, dx in dir:
                ny = pos[0]+dy
                nx = pos[1]+dx
                if 0 <= ny < height and 0<= nx < width and board[ny][nx] == letters[0] and (ny,nx) not in seen:
                    seen.add((ny,nx))
                    result = bfs(letters[1:], (ny,nx))
                    if not result:
                        seen.remove((ny,nx))
                    found.append(result)
                    
            return True if True in found else False
        
        exist = []
        if word[0] in startLetter.keys():
            for p in startLetter.get(word[0]):
                seen.add(p)
                exist.append(bfs(word[1:], p))
                seen = set()
        
        return True in exist
        

if __name__ == "__main__":
    
    board = [["A","B","C","E"],
             ["S","F","E","S"],
             ["A","D","E","E"]]
    word = "ABCESEEEFS"
    
    s = Solution()
    print(s.exist(board, word))
    
    print("Running Solution...")
