from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = []

        def dfs(node):
            if node:
                dfs(node.left)
                smallest.append(node.val)
                dfs(node.right)

        dfs(root)

        if len(smallest) < k:
            return -1

        return smallest[k - 1]


if __name__ == "__main__":
    sol = Solution()
    root = deserialize([4, 3, 5, 2, null])
    k = 4
    print(sol.kthSmallest(root, k))
    print("Running Solution...")
