from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []

        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                results.append(node.val)

        dfs(root)
        return results

        pass


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
