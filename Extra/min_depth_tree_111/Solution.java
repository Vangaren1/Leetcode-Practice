package Extra.min_depth_tree_111;
import common.TreeNode;

class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;

        int depth = Integer.max(minDepth(root.left), minDepth(root.right));

        return 1 + depth;
    }
    public static void main(String[] args) {
        System.out.println("Running min_depth_tree_111...");
    }
}
