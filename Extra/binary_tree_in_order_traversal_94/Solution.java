package Extra.binary_tree_in_order_traversal_94;
import java.util.ArrayList;
import java.util.List;

import common.TreeNode;

class Solution {
    List<Integer> retList;
    public List<Integer> inorderTraversal(TreeNode root) {
        
        retList = new ArrayList<>();
        traverse(root);
        return retList;
    }

    public void traverse(TreeNode node){
        if ( node != null) {
            traverse(node.left);
            retList.add(node.val);
            traverse(node.right);
        }
    }

    public static void main(String[] args) {
        System.out.println("Running binary_tree_in_order_traversal_94...");
    }
}
