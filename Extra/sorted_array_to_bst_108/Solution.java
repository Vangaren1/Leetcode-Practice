package Extra.sorted_array_to_bst_108;
import java.util.Arrays;

import common.TreeNode;

class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        
        int mid = nums.length / 2;
        TreeNode node = new TreeNode(nums[mid]);

        int[] leftarray = Arrays.copyOfRange(nums, 0, mid);
        node.left = sortedArrayToBST(leftarray);

        int[] rightarray = Arrays.copyOfRange(nums, mid+1, nums.length);
        node.right = sortedArrayToBST(rightarray);

        return node;

    }
    public static void main(String[] args) {
        System.out.println("Running sorted_array_to_bst_108...");
    }
}
