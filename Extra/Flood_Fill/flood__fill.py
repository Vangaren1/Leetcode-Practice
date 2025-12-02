from typing import Optional, List
from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
        original = image[sr][sc]

        queue = deque()
        queue.append((sr, sc))

        while queue:
            y, x = queue.popleft()

            image[y][x] = color

            for dy, dx in diff:
                ny = y + dy
                nx = x + dx
                if (
                    0 <= ny < height
                    and 0 <= nx < width
                    and image[ny][nx] == original
                    and (ny, nx) not in queue
                ):
                    queue.append((ny, nx))

        return image


if __name__ == "__main__":
    sol = Solution()
    image = [
        [0, 0, 0],
        [0, 0, 0],
    ]
    print(sol.floodFill(image, 1, 0, 2))
    print("Running Solution...")
