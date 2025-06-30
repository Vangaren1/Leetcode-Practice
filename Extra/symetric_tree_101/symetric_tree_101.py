from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isSameTree(root.left, root.right)
    
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None) ^ (q == None) :
            return False
        if p and q:
            checkLeft = self.isSameTree(p.left, q.right)
            checkVal = p.val == q.val
            checkRight = self.isSameTree(p.left, q.right)
            return checkLeft and checkVal and checkRight
        return True


if __name__ == "__main__":
    print("Running Solution...")
