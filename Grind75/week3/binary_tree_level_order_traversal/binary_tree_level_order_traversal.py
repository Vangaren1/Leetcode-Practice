from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return results


if __name__ == "__main__":
    null = None
    root = [3,9,20,null,null,15,7]
    root = deserialize(root)
    s = Solution()
    
    print(s.levelOrder(root))    
    print("Running Solution...")
