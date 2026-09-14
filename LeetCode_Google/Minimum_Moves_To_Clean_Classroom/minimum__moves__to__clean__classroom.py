from typing import Optional, List
import heapq
from collections import defaultdict, deque


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        h = len(classroom)
        w = len(classroom[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        litter = {}
        start = None
        idx = 0

        for y in range(h):
            for x in range(w):
                if classroom[y][x] == "S":
                    start = (y, x)
                elif classroom[y][x] == "L":
                    litter[(y, x)] = idx
                    idx += 1

        # 1 bit means that litter still remains
        startMask = (1 << idx) - 1

        sy, sx = start

        # y, x, energy_left, litter_mask, moves
        dq = deque([(sy, sx, energy, startMask, 0)])

        seen = {(sy, sx, energy, startMask)}

        while dq:
            y, x, currEnergy, mask, moves = dq.popleft()

            if mask == 0:
                return moves

            if currEnergy == 0:
                continue

            for dy, dx in dirs:
                ny, nx = y + dy, x + dx

                if not (0 <= ny < h and 0 <= nx < w):
                    continue

                if classroom[ny][nx] == "X":
                    continue

                newEnergy = currEnergy - 1
                newMask = mask

                if classroom[ny][nx] == "L":
                    bit = litter[(ny, nx)]
                    newMask &= ~(1 << bit)

                if classroom[ny][nx] == "R":
                    newEnergy = energy

                state = (ny, nx, newEnergy, newMask)

                if state not in seen:
                    seen.add(state)
                    dq.append((ny, nx, newEnergy, newMask, moves + 1))

        return -1


if __name__ == "__main__":
    sol = Solution()
    classroom = [
        "L.S",
        "RXL",
    ]
    energy = 3
    print(sol.minMoves(classroom, energy))
    print("Running Solution...")


""" 
'S': Starting position of the student
'L': Litter that must be collected (once collected, the cell becomes empty)
'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
'X': Obstacle the student cannot pass through
'.': Empty space
"""
