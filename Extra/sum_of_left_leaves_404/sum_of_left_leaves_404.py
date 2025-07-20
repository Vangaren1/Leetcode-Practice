from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(n):
            if n: 
                return n.left == None and n.right == None
            return False
        total = 0
        if root:
            if root.left and isLeaf(root.left):
                total+= root.left.val
            total += self.sumOfLeftLeaves(root.left)
            total += self.sumOfLeftLeaves(root.right)
        return total

if __name__ == "__main__":
    sol = Solution()    
    null = None
    root = [1]
    print(sol.sumOfLeftLeaves(deserialize(root)))
    print("Running Solution...")
