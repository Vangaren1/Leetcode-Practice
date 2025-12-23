from typing import Optional, List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < (n - 1):
            return -1

        uf = self.UnionFind(n)

        for a, b in connections:
            uf.union(a, b)

        groups = set(uf.parent)

        return uf.components - 1

    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
            self.components = n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # path compression
            return self.parent[x]

        def union(self, a, b):
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return False

            # weighted union
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]
            self.components -= 1
            return True


if __name__ == "__main__":
    sol = Solution()
    n = 100
    connections = [
        [17, 51],
        [33, 83],
        [53, 62],
        [25, 34],
        [35, 90],
        [29, 41],
        [14, 53],
        [40, 84],
        [41, 64],
        [13, 68],
        [44, 85],
        [57, 58],
        [50, 74],
        [20, 69],
        [15, 62],
        [25, 88],
        [4, 56],
        [37, 39],
        [30, 62],
        [69, 79],
        [33, 85],
        [24, 83],
        [35, 77],
        [2, 73],
        [6, 28],
        [46, 98],
        [11, 82],
        [29, 72],
        [67, 71],
        [12, 49],
        [42, 56],
        [56, 65],
        [40, 70],
        [24, 64],
        [29, 51],
        [20, 27],
        [45, 88],
        [58, 92],
        [60, 99],
        [33, 46],
        [19, 69],
        [33, 89],
        [54, 82],
        [16, 50],
        [35, 73],
        [19, 45],
        [19, 72],
        [1, 79],
        [27, 80],
        [22, 41],
        [52, 61],
        [50, 85],
        [27, 45],
        [4, 84],
        [11, 96],
        [0, 99],
        [29, 94],
        [9, 19],
        [66, 99],
        [20, 39],
        [16, 85],
        [12, 27],
        [16, 67],
        [61, 80],
        [67, 83],
        [16, 17],
        [24, 27],
        [16, 25],
        [41, 79],
        [51, 95],
        [46, 47],
        [27, 51],
        [31, 44],
        [0, 69],
        [61, 63],
        [33, 95],
        [17, 88],
        [70, 87],
        [40, 42],
        [21, 42],
        [67, 77],
        [33, 65],
        [3, 25],
        [39, 83],
        [34, 40],
        [15, 79],
        [30, 90],
        [58, 95],
        [45, 56],
        [37, 48],
        [24, 91],
        [31, 93],
        [83, 90],
        [17, 86],
        [61, 65],
        [15, 48],
        [34, 56],
        [12, 26],
        [39, 98],
        [1, 48],
        [21, 76],
        [72, 96],
        [30, 69],
        [46, 80],
        [6, 29],
        [29, 81],
        [22, 77],
        [85, 90],
        [79, 83],
        [6, 26],
        [33, 57],
        [3, 65],
        [63, 84],
        [77, 94],
        [26, 90],
        [64, 77],
        [0, 3],
        [27, 97],
        [66, 89],
        [18, 77],
        [27, 43],
    ]

    print(sol.makeConnected(n, connections))
    print("Running Solution...")
