from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        maxFound = float("-inf")

        def dfs(node):
            nonlocal maxFound
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            allowToSplit = left + right + node.val
            maxChild = max(left, right, 0)
            maxFound = max(maxFound, allowToSplit, node.val, node.val + maxChild)
            return node.val + maxChild

        dfs(root)

        return maxFound


if __name__ == "__main__":
    sol = Solution()
    # root = [-15, 10, 20, null, null, 15, 5, -5]
    root = [2, -1]
    root = deserialize(root)

    print(sol.maxPathSum(root))
    print("Running Solution...")
