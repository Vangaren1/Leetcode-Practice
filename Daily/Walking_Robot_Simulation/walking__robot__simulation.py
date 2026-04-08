from typing import Optional, List
import heapq
from collections import defaultdict


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.posX = 0
        self.posY = 0
        self.directions = ["East", "North", "West", "South"]
        self.currDir = 0
        self.perimeter = 2 * width + 2 * height - 4
        self.moved = False

    def incX(self, val):
        self.posX += val

    def decX(self, val):
        self.posX -= val

    def incY(self, val):
        self.posY += val

    def decY(self, val):
        self.posY -= val

    def step(self, num: int) -> None:
        if num == 0:
            return

        self.moved = True

        func = {
            0: (lambda: self.width - self.posX - 1, self.incX),
            1: (lambda: self.height - self.posY - 1, self.incY),
            2: (lambda: self.posX, self.decX),
            3: (lambda: self.posY, self.decY),
        }

        n = num % self.perimeter
        if n == 0:
            n = self.perimeter

        while n:
            maxV, f = func[self.currDir]
            maxStep = maxV()

            if maxStep >= n:
                f(n)
                break
            else:
                f(maxStep)
                n -= maxStep
                self.currDir = (self.currDir + 1) % 4

    def getPos(self) -> List[int]:
        return [self.posX, self.posY]

    def getDir(self) -> str:
        if self.posX == 0 and self.posY == 0 and self.moved:
            return "South"
        return self.directions[self.currDir]


if __name__ == "__main__":
    sol = Robot(6, 3)
    sol.step(2)
    sol.step(2)
    print(sol.getDir())
    print(sol.getPos())
    sol.step(2)
    sol.step(1)
    sol.step(4)
    print(sol.getDir())
    print(sol.getPos())
    print("Running Solution...")
