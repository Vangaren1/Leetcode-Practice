from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
                return root
            self.insertIntoBST(root.left, val)
            return root

        if root.right is None:
            root.right = TreeNode(val)
            return root
        self.insertIntoBST(root.right, val)
        return root


if __name__ == "__main__":
    sol = Solution()
    root = [5, 3, 9, 1, 4]
    val = 6
    printTree(sol.insertIntoBST(deserialize(root), val))

    print("Running Solution...")
