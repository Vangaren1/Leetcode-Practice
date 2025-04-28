from typing import Optional
from common.treenode import TreeNode, deserialize


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = 0
        def depthFirstSearch(node):
            nonlocal maximum
            if not node:
                return -1
            left = depthFirstSearch(node.left)
            right = depthFirstSearch(node.right)
            maximum = max(maximum, left + right + 2)
            return 1 + max(left, right)
        depthFirstSearch(root)
        return maximum

if __name__ == "__main__":
    root = [1,2,3,4,5]
    root = deserialize(root)
    s = Solution()
    print(s.diameterOfBinaryTree(root))
    print("Running Solution...")
