from typing import Optional

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node: TreeNode):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
        if not root:
            return True
        leftDepth = depth(root.left)
        rightDepth = depth(root.right)
        if abs(leftDepth - rightDepth) > 1:
            return False
        leftCheck = self.isBalanced(root.left)
        rightCheck = self.isBalanced(root.right)
        return leftCheck and rightCheck
        
if __name__ == "__main__":
    null = None
    root = [3,9,20,null,null,15,7]
    root = deserialize(root)
    s = Solution()
    s.isBalanced(root)
    
    print("Running Solution...")
