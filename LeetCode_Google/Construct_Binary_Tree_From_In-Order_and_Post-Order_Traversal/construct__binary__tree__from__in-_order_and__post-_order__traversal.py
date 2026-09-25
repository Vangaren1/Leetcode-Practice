from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        # root in postorder is the last element.  for inorder, everything to the left of that
        # is to the left side of the root
        rootVal = postorder.pop()
        root = TreeNode(rootVal)

        rootIndex = inorder.index(rootVal)
        leftHalfInOrder = inorder[:rootIndex]
        rightHalfInOrder = inorder[rootIndex + 1 :]

        leftCount = len(leftHalfInOrder)
        leftHalfPostOrder = postorder[:leftCount]
        rightCount = len(rightHalfInOrder)
        rightHalfPostOrder = postorder[leftCount : rightCount + leftCount]

        root.left = self.buildTree(leftHalfInOrder, leftHalfPostOrder)
        root.right = self.buildTree(rightHalfInOrder, rightHalfPostOrder)
        return root

        pass


if __name__ == "__main__":
    sol = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    printTree(sol.buildTree(inorder, postorder))
    print("Running Solution...")
