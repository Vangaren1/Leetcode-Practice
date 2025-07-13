package Extra.binary_tree_paths_257;
import java.util.ArrayList;
import java.util.List;

import common.TreeNode;

class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> retVal = new ArrayList<>();
        if ( root == null ){
            return retVal;
        }    
        if ( root.left == null && root.right == null) {
            retVal.add(0, Integer.toString(root.val));
        }

        List<String> leftPaths = binaryTreePaths(root.left);
        for ( String path : leftPaths){
            String tmp = Integer.toString(root.val) + "->" + path;
            retVal.add(0,tmp);
        }
        List<String> rightPaths = binaryTreePaths(root.right);
        for ( String path : rightPaths){
            String tmp = Integer.toString(root.val) + "->" + path;
            retVal.add(0,tmp);
        }
        return retVal;
    }
    public static void main(String[] args) {
        System.out.println("Running binary_tree_paths_257...");
    }
}
