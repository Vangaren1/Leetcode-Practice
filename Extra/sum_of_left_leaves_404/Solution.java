package Extra.sum_of_left_leaves_404;
import common.TreeNode;

class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        int total = 0;
        if (root != null) {
            if ( root.left != null && root.left.left == null && root.left.right == null){
                total = total + root.left.val;
            }
            total = total + sumOfLeftLeaves(root.left);
            total = total + sumOfLeftLeaves(root.right);
        }
        return total;
    }
    public static void main(String[] args) {
        Solution s = new Solution();

        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        System.out.println(s.sumOfLeftLeaves(root));
        System.out.println("Running sum_of_left_leaves_404...");
    }
}
