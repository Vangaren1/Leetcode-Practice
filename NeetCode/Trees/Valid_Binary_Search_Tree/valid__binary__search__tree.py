from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, interval):
            if node is None:
                return True
            if node and (interval[0] >= node.val or interval[1] <= node.val):
                return False
            checkLeft = dfs(node.left, [interval[0], node.val])
            checkRight = dfs(node.right, [node.val, interval[1]])
            return checkLeft and checkRight

        return dfs(root, [float("-inf"), float("inf")])


if __name__ == "__main__":
    sol = Solution()
    root = deserialize([5, 4, 6, null, null, 3, 7])
    print(sol.isValidBST(root))
    # root = deserialize([1, 2, 3])
    # print(sol.isValidBST(root))
    print("Running Solution...")
