package Grind75.week5.lowest_common_ancestor_of_bst_236;
import common.TreeNode;

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if( root == null || root == p || root == q){
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        if( left == null ){
            return right;
        }

        if (right == null){
            return left;
        }
        return root;

    }

    public static void main(String[] args) {
        System.out.println("Running lowest_common_ancestor_of_bst_236...");
    }
}
