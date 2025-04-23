from typing import Optional

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(ptr: Optional[TreeNode]):
            if not ptr: return (True, 0)
            
            print("looking at node: {}".format(ptr.val))
            left = dfs(ptr.left)
            right = dfs(ptr.right)
            leftrightDiff = abs(left[1] - right[1]) <= 1
            
            balanced = left[0] and right[0] and leftrightDiff
            
            return (balanced, max(left[1], right[1]) + 1)
        
        return dfs(root)[0]
            
        
if __name__ == "__main__":
    null = None
    root = [3,9,20,null,null,15,7]
    root = deserialize(root)
    s = Solution()
    s.isBalanced(root)
    
    print("Running Solution...")
