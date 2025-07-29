from typing import Optional, List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gPtr = 0
        sPtr = 0

        count = 0
        while gPtr < len(g) and sPtr < len(s):
            if s[sPtr] >= g[gPtr]:
                count += 1
                gPtr += 1
            sPtr += 1

        return count


if __name__ == "__main__":
    sol = Solution()

    g = [1, 2, 3]
    s = [1, 1]
    print("test")
    print(sol.findContentChildren(g, s))

    g = [1, 2]
    s = [1, 2, 3]
    print(sol.findContentChildren(g, s))

    print("Running Solution...")
