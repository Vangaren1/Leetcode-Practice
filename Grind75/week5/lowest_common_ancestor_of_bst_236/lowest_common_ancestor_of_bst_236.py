from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left:
            return right
        if not right:
            return left 
        return root

if __name__ == "__main__":
    s = Solution()
    
    null = None
    root = [3,5,1,6,2,0,8,null,null,7,4]
    p = 5
    q = 1
    root = deserialize(root)
    print(s.lowestCommonAncestor(root, p, q))
    print("Running Solution...")
