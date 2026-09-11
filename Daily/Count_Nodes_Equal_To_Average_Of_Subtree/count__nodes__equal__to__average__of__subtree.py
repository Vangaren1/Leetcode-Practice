from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        counter = 0

        # returns (total, count)
        def countNode(node):
            nonlocal counter
            if not node:
                return (0, 0)
            total = node.val

            left = countNode(node.left)
            right = countNode(node.right)
            total += left[0]
            total += right[0]
            count = 1 + left[1] + right[1]
            if node.val == total // count:
                counter += 1
            return (total, count)

        countNode(root)
        return counter
        pass


if __name__ == "__main__":
    sol = Solution()
    root = [4, 8, 5, 0, 1, null, 6]
    root = deserialize(root)
    print(sol.averageOfSubtree(root))
    print("Running Solution...")
