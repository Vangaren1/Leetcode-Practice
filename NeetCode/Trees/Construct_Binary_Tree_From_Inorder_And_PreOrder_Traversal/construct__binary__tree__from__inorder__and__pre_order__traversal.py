from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder and inorder:
            root = TreeNode(preorder.pop(0))

            index = 0
            while inorder[index] != root.val:
                index += 1

            left = inorder[0:index]
            right = inorder[index + 1 :]

            leftPre = []
            for _ in range(len(left)):
                leftPre.append(preorder.pop(0))

            rightPre = preorder

            root.left = self.buildTree(leftPre, left)
            root.right = self.buildTree(rightPre, right)

            return root


if __name__ == "__main__":
    sol = Solution()
    preorder = [1, 2, 3, 4]
    inorder = [2, 1, 3, 4]

    sol.buildTree(preorder, inorder)
    print("Running Solution...")
