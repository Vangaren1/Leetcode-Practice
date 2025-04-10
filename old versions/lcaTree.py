# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insert(root, val):
    temp = TreeNode(val)
    if root is None:
        root = temp
        return root
    # if already exists in the root, do nothing
    if val == root.val:
        return root
    if val <= root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def traverse(tree):
    if tree is not None:
        traverse(tree.left)
        print(tree.val, end=" ")
        traverse(tree.right)

class Solution:
    def search(self, root, x):
        if root is None:
            return False
        if root.val == x:
            return True
        if root.val < x:
            return self.search(root.right, x)
        return self.search(root.left, x)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if the root value is p, and q can be found on any node under root, return root
        if root.val == p.val or root.val == q.val:
            return root
        else:
            # if p is on the left, and q is on the right, return root, also the reverse
            pLeft = self.search(root.left, p.val)
            qRight = self.search(root.right, q.val)
            pRight = self.search(root.right, p.val)
            qLeft = self.search(root.left, q.val)
            if (pLeft and qRight) or (qLeft and pRight):
                return root
            #if they're both on the left, check the lca for all the nodes on the left
            if pLeft and qLeft:
                return self.lowestCommonAncestor(root.left, p, q)
            # if they're both on the right, check the lca for all the nodes on the right
            if pRight and qRight:
                return self.lowestCommonAncestor(root.right, p, q)






root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)



obj=Solution()

print(obj.search(root, 2))

print(obj.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val)
