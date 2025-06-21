from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        results = []
        def traverse(root):
            if not root: 
                return
            traverse(root.left)
            results.append(root.val)
            traverse(root.right)
        traverse(root)
        return results[k-1]

if __name__ == "__main__":
    print("Running Solution...")
