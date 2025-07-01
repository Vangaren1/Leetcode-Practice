from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tmp = []
        if not root: 
            return tmp
        tmp.append(root.val)
        tmp = tmp + self.preorderTraversal(root.left)
        tmp = tmp + self.preorderTraversal(root.right)
        return tmp        

if __name__ == "__main__":
    s = Solution()
    null = None
    root = deserialize([1,2,3,4,5,null,8,null,null,6,7,9])
    
    print(s.preorderTraversal(root))
    print("Running Solution...")
