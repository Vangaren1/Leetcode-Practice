package Grind75.week2.diameter_of_binary_tree_543;

import common.TreeNode;

class Solution {
    public int maximum = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return maximum;   
    }

    public int dfs(TreeNode node){
        if(node == null){
            return -1;
        }
        int left = dfs(node.left);
        int right = dfs(node.right);
        maximum = Math.max(maximum, left + right + 2);
        return 1 + Math.max(left, right);
    }
    public static void main(String[] args) {
        System.out.println("Running diameter_of_binary_tree_543...");
    }
}
