package Grind75.week2.maximum_depth_of_binary_tree_104;
import common.TreeNode;


class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
    public static void main(String[] args) {
        System.out.println("Running maximum_depth_of_binary_tree_104...");
    }
}
