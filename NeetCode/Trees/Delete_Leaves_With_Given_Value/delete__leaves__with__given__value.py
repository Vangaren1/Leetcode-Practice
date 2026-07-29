from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.val != target:
            return root

        if root.val == target and root.left is None and root.right is None:
            return None

        return root


if __name__ == "__main__":
    sol = Solution()
    root = [1, 2, 3, 5, 2, 2, 5]
    root = deserialize(root)
    target = 2
    printTree(sol.removeLeafNodes(root, target))
    print("Running Solution...")
