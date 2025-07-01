from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False
        if root.val == targetSum and root.left == None and root.right == None:
            return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        

if __name__ == "__main__":
    s = Solution()
    null = None
    assert s.hasPathSum(deserialize([5,4,8,11,null,13,4,7,2,null,null,null,1]), 22) == True
    assert s.hasPathSum(deserialize([1,2,3]), 5) == False
    assert s.hasPathSum(deserialize([]), 0) == False
    assert s.hasPathSum(deserialize([1,2]), 1) == True
    print("Running Solution...")
