from typing import Optional

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ptr = root
        while True:
            if ptr.val > p.val and ptr.val > q.val:
                ptr = ptr.left
            elif ptr.val < p.val and ptr.val < q.val:
                ptr = ptr.right
            else:
                return ptr

if __name__ == "__main__":
    null = None
    root = [6,2,8,0,4,7,9,null,null,3,5]
    p = 2
    q = 8
    s = Solution()
    root = deserialize(root)
    
    s.lowestCommonAncestor(root, TreeNode(p), TreeNode(q))
    
    print("Running Solution...")
