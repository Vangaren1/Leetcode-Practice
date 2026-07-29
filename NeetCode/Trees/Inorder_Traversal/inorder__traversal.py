from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def trav(node):
            if node is None:
                return None

            trav(node.left)
            result.append(node.val)
            trav(node.right)

        trav(root)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
