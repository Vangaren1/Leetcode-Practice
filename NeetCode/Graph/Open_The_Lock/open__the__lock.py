from typing import Optional, List
import heapq
from collections import defaultdict, deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        upDown = {
            "0": ("9", "1"),
            "1": ("0", "2"),
            "2": ("1", "3"),
            "3": ("2", "4"),
            "4": ("3", "5"),
            "5": ("4", "6"),
            "6": ("5", "7"),
            "7": ("6", "8"),
            "8": ("7", "9"),
            "9": ("8", "0"),
        }
        visited = set(["0000"])
        dead = set(deadends)
        queue = deque()
        if "0000" not in dead:
            queue.append(("0000", 0))

        while queue:

            curr, dist = queue.popleft()
            curr = [ch for ch in curr]

            for i in range(4):
                original = curr[i]
                pair = upDown[original]
                curr[i] = pair[0]
                up = "".join(curr)
                if up == target:
                    return dist + 1
                curr[i] = pair[1]
                down = "".join(curr)
                if down == target:
                    return dist + 1
                curr[i] = original
                if up not in dead and up not in visited:
                    visited.add(up)
                    queue.append((up, dist + 1))
                if down not in dead and down not in visited:
                    visited.add(down)
                    queue.append((down, dist + 1))

        return -1

        pass


if __name__ == "__main__":
    sol = Solution()
    deadends = ["1111", "0120", "2020", "3333"]
    target = "5555"
    print(sol.openLock(deadends, target))
    print("Running Solution...")


""" 
literally did this the hardest way possible lol

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getDigit(num, pos):
            tmp = num // 10**pos
            return tmp % 10

        # store the end points using an adjacency map
        adj = defaultdict(list)

        for i in range(10000):
            # get each digit
            digits = [getDigit(i, d) for d in range(4)]
            for pos in range(4):
                # store original
                original = digits[pos]
                digits[pos] = (original + 1) % 10
                up = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0]
                digits[pos] = (original + 9) % 10
                down = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0]
                # store edge in adj
                adj[i].append(up)
                adj[i].append(down)
                # restore original
                digits[pos] = original

        # remove the deadends edges
        for dead in deadends:
            adj[int(dead)] = []

        # use shortest path/ djsktra's algorithm

        dist = [float("inf") for _ in range(10000)]
        pq = []

        dist[0] = 0
        heapq.heappush(pq, (0, 0))

        while pq:
            distance, node = heapq.heappop(pq)

            if distance > dist[node]:
                continue

            for neighbor in adj[node]:
                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    heapq.heappush(pq, (dist[neighbor], neighbor))

        return dist[int(target)] if dist[int(target)] != float("inf") else -1

"""
