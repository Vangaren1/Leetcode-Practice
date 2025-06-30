from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None) ^ (q == None) :
            return False
        if p and q:
            checkLeft = self.isSameTree(p.left, q.left)
            checkVal = p.val == q.val
            checkRight = self.isSameTree(p.right, q.right)
            return checkLeft and checkVal and checkRight
        return True

if __name__ == "__main__":
    
    p = deserialize([1,None,2])
    q = deserialize([1,None,2])
    
    s = Solution()
    print(s.isSameTree(p,q))
    print("Running Solution...")
