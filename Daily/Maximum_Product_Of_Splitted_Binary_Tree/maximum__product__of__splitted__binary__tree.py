from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        maxSeen = float("-inf")

        seenNodes = {}

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            if node in seenNodes:
                return seenNodes[node]
            left = dfs(node.left)
            right = dfs(node.right)
            total = node.val + left + right
            seenNodes[node] = total
            return total

        total = dfs(root)

        for value in seenNodes.values():
            maxSeen = max(maxSeen, (total - value) * value)

        return maxSeen % (10**9 + 7)


if __name__ == "__main__":
    sol = Solution()
    root = deserialize([1, 2, 3, 4, 5, 6])
    print(sol.maxProduct(root))

    root = [1, null, 2, 3, 4, null, null, 5, 6]
    root = deserialize(root)
    print(sol.maxProduct(root))
    print("Running Solution...")
