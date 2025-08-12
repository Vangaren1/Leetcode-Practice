from typing import Optional, List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def colide(a, b):
            # returns true if A arrives before B or at the same time
            arriveA = (target - a[0]) / a[1]
            arriveB = (target - b[0]) / b[1]
            return arriveA <= arriveB

        posM = []

        for index, pos in enumerate(position):
            s = speed[index]
            posM.append((pos, s))

        posM.sort(key=lambda x: x[0], reverse=True)

        carStack = []
        for car in posM:
            carStack.append(car)
            if len(carStack) > 1 and colide(carStack[-1], carStack[-2]):
                carStack.pop()

        return len(carStack)


if __name__ == "__main__":
    sol = Solution()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]

    print(sol.carFleet(target, position, speed))
    print("Running Solution...")
