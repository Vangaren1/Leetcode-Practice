from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSums = [0]

        def dfs(node, level):
            if node:
                if len(levelSums) < level:
                    levelSums.append(0)
                dfs(node.left, level + 1)

                levelSums[level - 1] += node.val

                dfs(node.right, level + 1)

        dfs(root, 1)

        maxVal = max(levelSums)

        return levelSums.index(maxVal)
        pass


if __name__ == "__main__":
    sol = Solution()
    root = [1, 7, 0, 7, -8, null, null]
    root = deserialize(root)

    print(sol.maxLevelSum(root))
    print("Running Solution...")
