from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        if root1 == None and root2 == None:
            return None

        if root2 == None and root1:
            return root1
        if root1 == None and root2:
            return root2

        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


if __name__ == "__main__":
    sol = Solution()
    root1 = [1, 3, 2, 5]
    root2 = [2, 1, 3, null, 4, null, 7]
    root1 = deserialize(root1)
    root2 = deserialize(root2)

    printTree(sol.mergeTrees(root1, root2))
    print("Running Solution...")
