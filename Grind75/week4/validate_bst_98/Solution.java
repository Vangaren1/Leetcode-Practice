package Grind75.week4.validate_bst_98;

import common.TreeNode;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean isValidBST(TreeNode root) {
        return traverse(root, new ArrayList<Integer>(), new ArrayList<Integer>());    
    }

    public boolean traverse(TreeNode node, ArrayList<Integer> left, ArrayList<Integer> right){
        if ( node == null){
            return true;
        }
        for( int l: left){
            if (node.val >= l){
                return false;
            }
        }
        for (int r: right){
            if ( node.val <= r){
                return false;
            }
        }

        left.add(0, node.val);
        if (!traverse(node.left, left, right)){
            return false;
        }

        left.remove(0);
        right.add(0, node.val);
        if (!traverse(node.right, left, right)){
            return false;
        }

        return true;
    }
    public static void main(String[] args) {

        Solution s = new Solution();



        System.out.println("Running validate_bst_98...");
    }
}
