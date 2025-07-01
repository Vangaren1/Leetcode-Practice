package Extra.binary_tree_preorder_traversal_144;
import java.util.ArrayList;
import java.util.List;

import common.TreeNode;

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> tmp = new ArrayList<>();
        if (root == null) {
            return tmp;
        }    
        tmp.add(root.val);
        tmp.addAll(preorderTraversal(root.left));
        tmp.addAll(preorderTraversal(root.right));
        return tmp;
    }
    public static void main(String[] args) {
        System.out.println("Running binary_tree_preorder_traversal_144...");
    }
}
