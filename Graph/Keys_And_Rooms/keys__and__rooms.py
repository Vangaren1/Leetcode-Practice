from typing import Optional, List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        open = [False] * n
        open[0] = True

        visited = set()

        def dfs(node):
            if not open[node]:
                return
            visited.add(node)
            for door in rooms[node]:
                if door not in visited:
                    open[door] = True
                    dfs(door)

        dfs(0)

        return not (False in open)


if __name__ == "__main__":
    sol = Solution()
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(sol.canVisitAllRooms(rooms))

    rooms = [
        [6, 7, 8],
        [5, 4, 9],
        [],
        [8],
        [4],
        [],
        [1, 9, 2, 3],
        [7],
        [6, 5],
        [2, 3, 1],
    ]
    print(sol.canVisitAllRooms(rooms))
    print("Running Solution...")
