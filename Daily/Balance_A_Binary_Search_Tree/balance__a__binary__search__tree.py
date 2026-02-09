from typing import Optional, List
import heapq, math
from collections import defaultdict

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        psuedo, size = self.treeToVine(root)
        self.vineToTree(psuedo, size).right
        return psuedo.right

    def treeToVine(self, root):
        pseudo = TreeNode(-1)
        pseudo.right = root
        size = 0
        tail = pseudo
        rest = root
        while rest:
            if rest.left is None:
                tail = rest
                rest = tail.right
                size += 1
            else:
                tmp = rest.left
                rest.left = tmp.right
                tmp.right = rest
                rest = tmp
                tail.right = tmp

        return pseudo, size

    def vineToTree(self, root, size):
        h = (size + 1).bit_length() - 1
        m = (1 << h) - 1
        leaves = size - m

        self.compress(root, leaves)

        while m > 1:
            m //= 2
            self.compress(root, m)

        return root

    def compress(self, root, count):
        scanner = root
        for _ in range(count):
            child = scanner.right
            if not child:
                break
            scanner.right = child.right
            if not scanner.right:
                break
            scanner = scanner.right
            child.right = scanner.left
            scanner.left = child


"""

routine compress(root, count)
    scanner ← root
    for i ← 1 to count
        child ← scanner.right
        scanner.right ← child.right
        scanner ← scanner.right
        child.right ← scanner.left
        scanner.left ← child
"""

if __name__ == "__main__":
    sol = Solution()
    root = deserialize([2, 1, 3])
    printTree(sol.balanceBST(root))
    print("Running Solution...")
