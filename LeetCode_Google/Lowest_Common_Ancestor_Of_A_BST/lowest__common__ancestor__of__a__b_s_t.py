from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":

        nodeSet = set(nodes)

        def dfs(node):
            if not node:
                return

            if node in nodeSet:
                return node

            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node

            return left if left else right

        return dfs(root)


if __name__ == "__main__":
    sol = Solution()
    root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
    nodes = [4, 7]
    root = deserialize(root)

    print(sol.lowestCommonAncestor(root, nodes))
    print("Running Solution...")
