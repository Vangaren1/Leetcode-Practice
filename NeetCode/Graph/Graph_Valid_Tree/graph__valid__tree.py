from typing import Optional, List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        qu = self.QUFind(n)
        for a, b in edges:
            check = qu.union(a, b)
            if not check:
                return False
        return all([i == qu.array[0] for i in qu.array])

    class QUFind:
        def __init__(self, n):
            self.array = [i for i in range(n)]

        def connected(self, a, b):
            return self.array[a] == self.array[b]

        def union(self, a, b):
            currA = self.array[a]
            currB = self.array[b]
            if currA == currB:
                return False
            for index in range(len(self.array)):
                if self.array[index] == currA:
                    self.array[index] = currB
            return True


if __name__ == "__main__":
    sol = Solution()
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(sol.validTree(5, edges))
    print("Running Solution...")
