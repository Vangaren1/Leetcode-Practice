from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            newRoot = TreeNode(root.val)
            newRoot.left = self.invertTree(root.right)
            newRoot.right = self.invertTree(root.left)
            return newRoot


if __name__ == "__main__":
    sol = Solution()
    root = deserialize([1, 2, 3, 4, 5, 6, 7])
    printTree(sol.invertTree(root))
    print("Running Solution...")
