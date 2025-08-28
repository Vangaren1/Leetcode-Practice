from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        ptr = root

        while True:
            if ptr.val < p.val and ptr.val < q.val:
                ptr = ptr.right
            elif ptr.val > p.val and ptr.val > q.val:
                ptr = ptr.left
            else:
                return ptr


if __name__ == "__main__":
    sol = Solution()
    root = deserialize([5, 3, 8, 1, 4, 7, 9, null, 2])

    p = root.left
    q = root.right

    print(sol.lowestCommonAncestor(root, p, q).val)

    print("Running Solution...")
