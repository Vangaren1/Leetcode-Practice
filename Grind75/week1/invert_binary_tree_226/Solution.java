package Grind75.week1.invert_binary_tree_226;



class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root != null){
            TreeNode newRoot = new TreeNode(root.val);
            newRoot.left = invertTree(root.right);
            newRoot.right = invertTree(root.left);
            return newRoot;
        }
        return root;
    }

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }


    
    public static void printTree(TreeNode root){
        printTreeRecursive(root);
        System.out.println();
    }

    public static void printTreeRecursive(TreeNode root) {
        if (root == null) return;
        printTreeRecursive(root.left);
        System.out.print(root.val + " ");
        printTreeRecursive(root.right);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        
        TreeNode root = s.new TreeNode(2, s.new TreeNode(1), s.new TreeNode(3));
      
        Solution.printTree(root);

        root = s.invertTree(root);
        
        Solution.printTree(root);

        System.out.println("Running invert_binary_tree-226...");
    }
}
