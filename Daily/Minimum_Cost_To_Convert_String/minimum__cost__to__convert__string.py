from typing import Optional, List
import heapq


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        def idx(ch):
            return ord(ch) - ord("a")

        INF = float("inf")
        n = 26

        dist = [[INF] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        edges = []
        for index, ch in enumerate(original):
            edges.append((idx(ch), idx(changed[index]), cost[index]))

        for org, chg, cost in edges:
            dist[org][chg] = min(dist[org][chg], cost)

        for x in range(n):
            for y in range(n):
                if dist[y][x] == INF:
                    continue
                for z in range(n):
                    if dist[x][z] == INF:
                        continue
                    if dist[y][x] + dist[x][z] < dist[y][z]:
                        dist[y][z] = dist[y][x] + dist[x][z]

        total = 0

        for index, ch in enumerate(source):
            fromCh = idx(ch)
            toCh = idx(target[index])
            if dist[fromCh][toCh] == INF:
                return -1
            total += dist[fromCh][toCh]

        return total


if __name__ == "__main__":
    sol = Solution()
    source = "abcd"
    target = "acbe"
    original = ["a", "b", "c", "c", "e", "d"]
    changed = ["b", "c", "b", "e", "b", "e"]
    cost = [2, 5, 5, 1, 2, 20]

    print(sol.minimumCost(source, target, original, changed, cost))
    print("Running Solution...")
