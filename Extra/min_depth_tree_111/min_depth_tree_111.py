from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def recur(root):
            if root and root.left == None and root.right == None:
                return 1
            
            if not root:
                return float('inf')

            left = recur(root.left)
            right = recur(root.right)
            return 1 + min(left, right)
        return recur(root)

if __name__ == "__main__":
    s = Solution()
    null = None
    root1 = deserialize([3,9,20,null,null,15,7])
    root2 = deserialize([2,null,3,null,4,null,5,null,6])
    root3 = deserialize([])
    assert s.minDepth(root1) == 2
    assert s.minDepth(root2) == 5
    assert s.minDepth(root3) == 0
    
    print("Running Solution...")
