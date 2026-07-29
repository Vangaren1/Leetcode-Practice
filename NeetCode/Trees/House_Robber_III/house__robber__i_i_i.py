from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # return (canRob, cantRob)
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            canRob = node.val + left[1] + right[1]
            dontRob = max(left) + max(right)

            return (canRob, dontRob)

        return max(dfs(root))


if __name__ == "__main__":
    sol = Solution()
    root = [4, 1, null, 2, null, 3]
    root = deserialize(root)

    print(sol.rob(root))
    print("Running Solution...")
