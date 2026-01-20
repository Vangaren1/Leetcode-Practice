from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        results = []

        def dfs(node: Optional[TreeNode], level):
            if node:
                if len(results) < level:
                    results.append([])
                results[level - 1].append(node.val)
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 1)
        return [sum(level) / len(level) for level in results]


if __name__ == "__main__":
    sol = Solution()
    root = deserialize([3, 9, 20, null, null, 15, 7])
    print(sol.averageOfLevels(root))
    print("Running Solution...")
