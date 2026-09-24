from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        levels = defaultdict(list)

        def traverse(node, level):
            if not node:
                return

            traverse(node.left, level + 1)
            levels[level].append(node.val)
            traverse(node.right, level + 1)

        traverse(root, 0)

        results = []

        for i in range(len(levels)):
            if i % 2 == 0:
                results.append(levels[i])
            else:
                results.append(levels[i][::-1])
        return results

        pass


if __name__ == "__main__":
    sol = Solution()
    root = [3, 9, 20, null, null, 15, 7]
    root = deserialize(root)

    print(sol.zigzagLevelOrder(root))
    print("Running Solution...")
