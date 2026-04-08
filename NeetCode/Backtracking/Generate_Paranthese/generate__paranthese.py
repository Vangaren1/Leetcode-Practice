from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def dfs(s, opened, closed):
            if len(s) == 2 * n:
                results.append(s)

            if opened < n:
                dfs(s + "(", opened + 1, closed)

            if closed < opened:
                dfs(s + ")", opened, closed + 1)

        dfs("", 0, 0)

        return results


if __name__ == "__main__":
    sol = Solution()
    for i in range(5):
        print(sol.generateParenthesis(i))
    print("Running Solution...")
