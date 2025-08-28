from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = []

        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr:
                nodes.append(str(curr.val)) if curr != "N" else nodes.append("N")
                if curr != "N":
                    queue.append(curr.left) if curr.left else queue.append("N")
                    queue.append(curr.right) if curr.right else queue.append("N")

        while nodes and nodes[-1] == "N":
            nodes.pop()

        return "/".join(nodes)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        nodes = data.split("/")

        nodes = [int(n) if n != "N" else None for n in nodes]

        if len(nodes) == 0:
            return None

        root = TreeNode(nodes.pop(0))
        queue = [root]
        while queue:
            curr = queue.pop(0)

            if nodes:
                left = nodes.pop(0)
                if left != None:
                    curr.left = TreeNode(left)
                    queue.append(curr.left)

            if nodes:
                right = nodes.pop(0)
                if right != None:
                    curr.right = TreeNode(right)
                    queue.append(curr.right)

        return root


if __name__ == "__main__":
    sol = Codec()

    root = [
        4,
        -7,
        -3,
        null,
        null,
        -9,
        -3,
        9,
        -7,
        -4,
        null,
        6,
        null,
        -6,
        -6,
        null,
        null,
        0,
        6,
        5,
        null,
        9,
        null,
        null,
        -1,
        -4,
        null,
        null,
        null,
        -2,
    ]
    root = deserialize(root)

    s = sol.serialize(root)
    print(s)

    r = sol.deserialize(s)
    printTree(r)

    print("Running Solution...")
