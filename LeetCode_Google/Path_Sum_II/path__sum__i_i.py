from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []

        def recursive(node, currPath, currSum):
            if not node:
                return

            currPath.append(node.val)
            if (
                currSum + node.val == targetSum
                and node.left == None
                and node.right == None
            ):
                paths.append(currPath[:])
                return

            recursive(node.left, currPath[:], currSum + node.val)
            recursive(node.right, currPath[:], currSum + node.val)

        recursive(root, [], 0)
        return paths


if __name__ == "__main__":
    sol = Solution()
    root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
    targetSum = 22
    root = deserialize(root)

    print(sol.pathSum(root, targetSum))

    print("Running Solution...")
