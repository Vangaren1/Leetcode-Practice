from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:

            if p.val != q.val:
                return False

            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        if p is None and q is None:
            return True

        return False


if __name__ == "__main__":
    sol = Solution()
    p = deserialize([1, 2, 3])
    q = deserialize([1, 2, 3])
    print(sol.isSameTree(p, q))
    print("Running Solution...")
