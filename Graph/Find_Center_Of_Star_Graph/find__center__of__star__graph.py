from typing import Optional, List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for source, dest in edges:
            if source in seen:
                return source
            if dest in seen:
                return dest
            seen.add(source)
            seen.add(dest)

        pass


if __name__ == "__main__":
    sol = Solution()
    edges = [[1, 2], [2, 3], [4, 2]]
    print(sol.findCenter(edges))
    print("Running Solution...")
