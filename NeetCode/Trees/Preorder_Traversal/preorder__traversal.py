from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []

        def trav(node):
            if node:
                results.append(node.val)
                trav(node.left)
                trav(node.right)

        trav(root)
        return results
        pass


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
