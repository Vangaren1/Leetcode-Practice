from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maximum):
            nonlocal count
            if node:
                if node.val > maximum:
                    count += 1
                newMax = max(maximum, node.val)
                dfs(node.left, newMax)
                dfs(node.right, newMax)

        dfs(root, float("-inf"))
        return count


if __name__ == "__main__":
    sol = Solution()
    root = [3, 3, null, 4, 2]
    root = deserialize(root)
    print(sol.goodNodes(root))
    print("Running Solution...")
