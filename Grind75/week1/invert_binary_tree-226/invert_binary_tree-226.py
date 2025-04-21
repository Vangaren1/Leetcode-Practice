from typing import Optional

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass 
    
    pass

if __name__ == "__main__":
    root = [4,2,7,1,3,6,9]

    s = Solution()
    root = deserialize(root)
    
    printTree(root)
    
    
    print("Running Solution...")
