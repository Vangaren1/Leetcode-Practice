from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recIsValid(root, vals):
            if root is None:
                return (True,[])
            checkLeft = self.isValidBST(root.left)
            if not checkLeft[0]: 
                return (False, [])
            for v in checkLeft[1]:
                if root.val < v:
                    return (False, [])
            if root.left and root.val < root.left.val:
                return (False, [])
            
            checkRight = self.isValidBST(root.right)
            if not checkRight[0]:
                return (False, [])
            for v in checkRight[1]:
                if root.val > v:
                    return (False, [])
            if root.right and root.val > root.right.val:
                return (False, [])
            
            vals.append(root.val)
            return (True, vals)
        return recIsValid(root, [])


if __name__ == "__main__":
    s= Solution()
    null = None
    root = [5,4,6,null,null,3,7]
    root = deserialize(root)
    
    print(s.isValidBST(root))
    
    print("Running Solution...")
