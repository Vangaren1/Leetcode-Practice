# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        def build(r, base, rList):
            if base == "":
                connector = ""
            else:
                connector = "->"
            if r is None:
                return base
            if r.left is None and r.right is None:
                rList.add(base + connector + str(r.val))
                return rList
            rlist = []
            if r.left is not None and r.right is None:
                rList.union(build(r.left, base + connector +str(r.val), rList))
                return rList
            if r.right is not None and r.left is None:
                rList.union(build(r.right, base + connector +str(r.val), rList))
                return rList
            rList.union(build(r.left, base + connector +str(r.val), rList))
            rList.union(build(r.right, base + connector +str(r.val), rList))
            return rList
        return list(build(root, "", set()))







obj = Solution()

test1 = TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=5)), right = TreeNode(val=3))
test2 = TreeNode(val=1, left=TreeNode(val=2))

print(obj.binaryTreePaths(test1))
