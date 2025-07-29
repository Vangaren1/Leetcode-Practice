from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        base = ""
        n = None
        if not root:
            return base
        queue = [root]
        while queue:
            curr = queue.pop()
            if curr is None:
                base += "/N"
            else:
                base += "/" + str(curr.val)
                queue.insert(0, curr.left)
                queue.insert(0, curr.right)
        return base

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        array = data.split("/")
        array.pop(0)

        nodes = [TreeNode(int(t)) if t != "N" else None for t in array]
        childNodes = nodes[::-1]
        root = childNodes.pop()
        for node in nodes:
            if node:
                if childNodes:
                    node.left = childNodes.pop()
                if childNodes:
                    node.right = childNodes.pop()
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == "__main__":
    null = None
    root = deserialize([1, 2, 3, null, null, 4, 5])
    s = Codec()
    output = s.serialize(root)
    print(output)
    print("Running Solution...")
