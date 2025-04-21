from typing import Optional
from common.treenode import TreeNode, deserialize, printTree



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            newRoot = TreeNode(val = root.val)
            newRoot.left = self.invertTree(root.right)
            newRoot.right = self.invertTree(root.left)
            return newRoot
        

if __name__ == "__main__":
    root = [4,2,7,1,3,6,9]

    s = Solution()
    root = deserialize(root)
    
    printTree(root)
    
    printTree(s.invertTree(root))
    
    print("Running Solution...")
