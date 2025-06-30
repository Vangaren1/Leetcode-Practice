package Extra.same_tree_100;
import common.TreeNode;

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        boolean checkLeft, checkVal, checkRight;
        if ((p==null) ^ (q==null)){
            return false;
        }
        if (p!=null && q != null){
             checkLeft = isSameTree(p.left, q.left);
             checkVal = p.val == q.val;
             checkRight = isSameTree(p.right, q.right);
             return checkLeft && checkVal && checkRight;
        }   
        return true;
    }
    public static void main(String[] args) {
        System.out.println("Running same_tree_100...");
    }
}
