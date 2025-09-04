from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        pathNums = []

        def getPath(node: Optional[TreeNode], s):
            if node:
                curr = s + str(node.val)
                if node.left == None and node.right == None:
                    pathNums.append(curr)
                else:
                    getPath(node.left, curr)
                    getPath(node.right, curr)

        getPath(root, "")

        return sum([int(num) for num in pathNums])


if __name__ == "__main__":
    sol = Solution()
    root = deserialize([2, 0, 0])
    print(sol.sumNumbers(root))
    print("Running Solution...")
