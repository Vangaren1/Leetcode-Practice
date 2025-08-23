from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    heights = {}

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def height(node: TreeNode):
            if node is None:
                return 0
            self.heights[node] = 1 + max(height(node.left), height(node.right))
            return self.heights[node]

        leftH = height(root.left)
        rightH = height(root.right)

        heightBalanced = abs(leftH - rightH) <= 1

        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)

        return heightBalanced and leftBalanced and rightBalanced


if __name__ == "__main__":
    sol = Solution()
    root = [1, 2, 3, null, null, 4, null, 5]
    root = deserialize(root)
    print(sol.isBalanced(root))
    print("Running Solution...")
