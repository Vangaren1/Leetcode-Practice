package Grind75.week8.kth_smallest_elementa_in_a_bst_230;
import java.util.ArrayList;
import java.util.List;

import common.TreeNode;

class Solution {
    List<Integer> results;
    public int kthSmallest(TreeNode root, int k) {
        results = new ArrayList<>();
        traverse(root);
        return results.get(k-1);

    }

    public void traverse(TreeNode root) {
        if (root != null) {
            traverse(root.left);
            results.add(root.val);
            traverse(root.right);
        }
    }
    public static void main(String[] args) {
        System.out.println("Running kth_smallest_elementa_in_a_bst_230...");
    }
}
