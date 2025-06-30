from typing import Optional, List

from common.treenode import TreeNode, deserialize, printTree

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        mid = (len(nums)) // 2
        
        
        node = TreeNode(val=nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    s = Solution()
    
    print(s.sortedArrayToBST(nums))
    tree = s.sortedArrayToBST(nums)
    printTree(tree)
    print("Running Solution...")
