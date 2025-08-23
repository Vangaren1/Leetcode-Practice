from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    sol = Solution()
    null = None
    root = []
    root = deserialize(root)

    print(sol.maxDepth(root))
    print("Running Solution...")
