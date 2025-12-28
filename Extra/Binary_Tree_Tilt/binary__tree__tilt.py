from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftTilt = self.findTilt(root.left)
        rightTilt = self.findTilt(root.right)
        if root.left:
            leftVal = root.left.val
        else:
            leftVal = 0

        if root.right:
            rightVal = root.right.val
        else:
            rightVal = 0

        rootTilt = abs(leftVal - rightVal) + leftTilt + rightTilt

        return rootTilt
        pass


if __name__ == "__main__":
    sol = Solution()
    root = [4, 2, 9, 3, 5, null, 7]
    root = deserialize(root)
    print(sol.findTilt(root))
    print("Running Solution...")
