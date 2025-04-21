package Grind75.week1.invert_binary_tree_226;
import java.util.Arrays;

import common.TreeNode;



class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root != null){
            

        }
        return root;
    }

    public static void main(String[] args) {
        
        TreeNode root = TreeNode.deserialize(Arrays.asList(4, 2, 7, 1, 3, 6, 9));
        TreeNode.printTree(root);  // Should print: 1 2 3 4 6 7 9

        System.out.println("Running invert_binary_tree-226...");
    }
}
