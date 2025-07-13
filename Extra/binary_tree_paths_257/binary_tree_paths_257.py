from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [str(root.val)]
        
        retVal = []
        for left_paths in self.binaryTreePaths(root.left):
            retVal.append(str(root.val)+"->"+left_paths)
        for right_paths in self.binaryTreePaths(root.right):
            retVal.append(str(root.val)+"->"+right_paths)
        return retVal


if __name__ == "__main__":
    s = Solution()
    
    
    
    null = None
    root = [1]
    root = deserialize(root)
    
    print(s.binaryTreePaths(root))
    
    print("Running Solution...")
