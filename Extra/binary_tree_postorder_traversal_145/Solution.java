package Extra.binary_tree_postorder_traversal_145;
import java.util.ArrayList;
import java.util.List;

import common.TreeNode;

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> tmp = new ArrayList<>();
        if (root == null) {
            return tmp;
        }    
        tmp.addAll(postorderTraversal(root.left));
        tmp.addAll(postorderTraversal(root.right));
        tmp.add(root.val);
        return tmp;
    }
    public static void main(String[] args) {
        System.out.println("Running binary_tree_postorder_traversal_145...");
    }
}
