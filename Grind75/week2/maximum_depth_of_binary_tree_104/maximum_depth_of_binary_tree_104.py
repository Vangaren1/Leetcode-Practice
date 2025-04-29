from typing import Optional

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    print("Running Solution...")
