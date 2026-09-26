from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def findLeaves(self, root: TreeNode | None) -> list[list[int]]:
        results = []
        curr = []

        def prune(node):
            if not node:
                return

            if not node.left and not node.right:
                curr.append(node.val)
                return

            node.left = prune(node.left)
            node.right = prune(node.right)

            return node

        while root:

            root = prune(root)

            results.append(curr[:])
            curr = []

        return results

        pass


if __name__ == "__main__":
    sol = Solution()
    root = [1, 2, 3, 4, 5]
    root = deserialize(root)
    print(sol.findLeaves(root))
    print("Running Solution...")
