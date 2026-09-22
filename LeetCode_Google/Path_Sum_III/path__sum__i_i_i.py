from typing import Optional, List
import heapq
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        count = 0

        def traverse(node, path):
            nonlocal count
            if not node:
                return

            newPath = path[:] + [node.val]
            total = 0
            foundOne = False
            for num in newPath[::-1]:
                total += num
                if not foundOne:
                    if total == targetSum:
                        count += 1
                        total = 0
                        foundOne = True
                elif foundOne and total == 0:
                    count += 1
                    break
            traverse(node.left, newPath)
            traverse(node.right, newPath)

        traverse(root, [])
        return count


if __name__ == "__main__":
    sol = Solution()
    root = [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1]
    targetSum = 8
    root = deserialize(root)
    print(sol.pathSum(root, targetSum))
    root = [0, 1, 1]
    targetSum = 1
    root = deserialize(root)
    print(sol.pathSum(root, targetSum))
    print("Running Solution...")
