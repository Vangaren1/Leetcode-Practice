from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if root is None:
            return 0
        return 1 + max([self.maxDepth(child) for child in root.children] + [0])


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
