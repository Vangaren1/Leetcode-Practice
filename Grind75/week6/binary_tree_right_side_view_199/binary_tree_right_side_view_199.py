from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        def traverse(node, level):
            nonlocal results
            if node:
                if len(results) < (level + 1):
                    results.append([])
                results[level].append(node.val)
                traverse(node.left, level + 1)
                traverse(node.right, level + 1)
        traverse(root, 0)        
        results = [ level[-1] for level in results ]
        return results
    pass


if __name__ == "__main__":
    null = None
    root = [3,9,20,null,null,15,7]
    root = deserialize(root)
    s = Solution()
    
    print(s.rightSideView(root))
    print("Running Solution...")
