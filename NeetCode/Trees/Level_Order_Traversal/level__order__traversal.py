from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        retList = []

        def bfs(node):
            queue = [(node, 0)]

            while queue:
                curr, level = queue.pop()
                if len(retList) < level + 1:
                    retList.append([])
                retList[level].append(curr.val)
                if curr.left:
                    queue.insert(0, (curr.left, level + 1))
                if curr.right:
                    queue.insert(0, (curr.right, level + 1))

        if root:
            bfs(root)

        return retList


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
