from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            # if the root is None, then it's a empty branch
            if root is None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.maximum = max(self.maximum, left + right + 2)
            return 1 + max(left, right)

        self.maximum = 0
        dfs(root)
        return self.maximum


if __name__ == "__main__":
    sol = Solution()
    root = [1, null, 2, 3, 4, 5]
    root = deserialize(root)
    print(sol.diameterOfBinaryTree(root))
    print("Running Solution...")
