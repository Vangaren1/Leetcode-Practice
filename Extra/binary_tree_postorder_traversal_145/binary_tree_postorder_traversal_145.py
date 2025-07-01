from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tmp = []
        if root is None:
            return tmp
        tmp = tmp + self.postorderTraversal(root.left)
        tmp = tmp + self.postorderTraversal(root.right)
        tmp.append(root.val)
        return tmp

if __name__ == "__main__":
    print("Running Solution...")
