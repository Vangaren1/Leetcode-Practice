from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []

        def dfs(node, level):
            if not node:
                return

            if len(results) < level + 1:
                results.append([])

            results[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return results


if __name__ == "__main__":
    sol = Solution()

    root = [3, 9, 20, null, null, 15, 7]
    root = deserialize(root)

    print(sol.levelOrder(root))
    print("Running Solution...")
