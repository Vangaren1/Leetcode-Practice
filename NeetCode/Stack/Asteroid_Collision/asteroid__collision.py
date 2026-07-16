from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < -asteroid:
                    # Existing asteroid is smaller.
                    stack.pop()
                elif stack[-1] == -asteroid:
                    # Both are destroyed.
                    stack.pop()
                    alive = False
                else:
                    # Incoming asteroid is smaller.
                    alive = False

            if alive:
                stack.append(asteroid)

        return stack


if __name__ == "__main__":
    sol = Solution()
    asteroids = [-2, -1, 1, 2]
    print(sol.asteroidCollision([2, 4, -4, -1]))
    print(sol.asteroidCollision([7, -3, 5]))
    print(sol.asteroidCollision([5, 5]))
    print(sol.asteroidCollision([-2, -1, 1, 2]))
    print("Running Solution...")
