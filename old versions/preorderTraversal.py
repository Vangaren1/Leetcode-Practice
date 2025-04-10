# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):
        def pT(root):
            if root is not None:
                if root.left is not None:
                    pT(root.left)
                if root.right is not None:
                    pT(root.right)
                results.append(root.val)
        results = []
        pT(root)
        return results



root = TreeNode(val=1)
root.right = TreeNode(val=2)
root.right.left = TreeNode(val=3)

s = Solution()

print(s.preorderTraversal(root))

