from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = None
        count = 0
        def traverse(root):
            nonlocal count, curr
            if not root: 
                return
            if count == k:
                return
            traverse(root.left)
            count += 1
            if count == k:
                curr = root.val
                return 
            traverse(root.right)
        traverse(root)
        return curr

if __name__ == "__main__":
    s = Solution()
    null = None
    root = [5,3,6,2,4,null,null,1]
    k = 3
    root = deserialize(root)
    print(s.kthSmallest(root, k))
    
    
    print("Running Solution...")
