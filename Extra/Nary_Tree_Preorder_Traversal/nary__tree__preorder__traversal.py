from typing import Optional, List


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        retVal = []

        def rec(root: "Node"):
            nonlocal retVal
            if root:
                retVal.append(root.val)
                for child in root.children:
                    rec(child)

        rec(root)
        return retVal


if __name__ == "__main__":
    sol = Solution()

    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    print(sol.preorder(root))
    print("Running Solution...")
