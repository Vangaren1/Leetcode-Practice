package Grind75.week1.balanced_binary_tree_110;
import common.TreeNode;

class Solution {
    public boolean isBalanced(TreeNode root) {
        DFSObj results = dfs(root);
        return results.b;
    }

    class DFSObj{
        boolean b;
        int height;
        DFSObj(boolean b, int height){
            this.b = b;
            this.height = height;
        }
    }

    public DFSObj dfs(TreeNode node){
        if(node == null){
            return new DFSObj(true, 0); 
        }

        DFSObj left = dfs(node.left);
        DFSObj right = dfs(node.right);

        int heightDiff = Math.abs( left.height - right.height);
        boolean balanced = heightDiff <= 1;
        balanced = balanced && left.b && right.b;
        
        int currHeight = Math.max(left.height, right.height) + 1;

        return new DFSObj(balanced, currHeight);
    }

    public static void main(String[] args) {
        System.out.println("Running balanced_binary_tree_110...");
    }
}
