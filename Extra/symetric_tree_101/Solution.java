package Extra.symetric_tree_101;
import common.TreeNode;

class Solution {
    public boolean isSymmetric(TreeNode root) {
        if ( root == null) return true;
        return isSameTree(root.left, root.right);
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        boolean checkLeft, checkVal, checkRight;
        if ((p==null) ^ (q==null)){
            return false;
        }
        if (p!=null && q != null){
             checkLeft = isSameTree(p.left, q.right);
             checkVal = p.val == q.val;
             checkRight = isSameTree(p.right, q.left);
             return checkLeft && checkVal && checkRight;
        }   
        return true;
    }

    public static void main(String[] args) {
        System.out.println("Running symetric_tree_101...");
    }
}
