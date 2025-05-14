from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node, left=[], right=[]) -> bool:
            if node is None:
                return True
            for l in left: 
                if node.val >= l:
                    return False
            for r in right:
                if node.val <= r:
                    return False
            
            checkLeft = traverse(node.left, left+[node.val], right)
            if not checkLeft:
                return False
            
            checkRight = traverse(node.right, left, right+[node.val])
            if not checkRight:
                return False
            
            return True
        
        result= traverse(root, [],[])
        return result

if __name__ == "__main__":
    
    s = Solution()
    
    root = [2,1,3]
    root = deserialize(root)
    assert s.isValidBST(root) == True
    
    null = None
    root = deserialize([5,1,4,null,null,3,6])
    assert s.isValidBST(root) == False
    
    
    print("Running Solution...")
