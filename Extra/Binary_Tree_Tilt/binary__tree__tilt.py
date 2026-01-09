from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def getSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return root.val + self.getSum(root.left) + self.getSum(root.right)

    def getTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return abs(self.getSum(root.left) - self.getSum(root.right))

    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        rootTilt = self.getTilt(root)
        leftTilt = self.findTilt(root.left)
        rightTilt = self.findTilt(root.right)

        return rootTilt + leftTilt + rightTilt


if __name__ == "__main__":
    sol = Solution()
    root = [4, 2, 9, 3, 5, null, 7]
    root = deserialize(root)
    print("results:")
    print(sol.findTilt(root))
    print("Running Solution...")
