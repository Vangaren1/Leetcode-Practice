from typing import Optional, List
import heapq

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        q = []

        def buildQ(node):
            if node:
                buildQ(node.left)
                heapq.heappush(q, node.val)
                buildQ(node.right)

        buildQ(root)
        first = heapq.heappop(q) if q else None
        prev = first

        while q and prev == first:
            prev = heapq.heappop(q)

        return prev if prev != first else -1


if __name__ == "__main__":
    sol = Solution()

    root = deserialize([2, 2, 5, null, null, 5, 7])
    print(sol.findSecondMinimumValue(root))
    print("Running Solution...")
