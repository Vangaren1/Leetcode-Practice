package common;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

//Definition for a binary tree node.
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


 // Deserialize: Build a binary tree from a level-order list
    public static TreeNode deserialize(List<Integer> values) {
        if (values == null || values.isEmpty()) return null;

        Queue<TreeNode> queue = new LinkedList<>();
        TreeNode root = new TreeNode(values.get(0));
        queue.offer(root);
        int i = 1;

        while (i < values.size()) {
            TreeNode current = queue.poll();
            if (current == null) continue;

            // Left child
            if (i < values.size() && values.get(i) != null) {
                current.left = new TreeNode(values.get(i));
                queue.offer(current.left);
            }
            i++;

            // Right child
            if (i < values.size() && values.get(i) != null) {
                current.right = new TreeNode(values.get(i));
                queue.offer(current.right);
            }
            i++;
        }

        return root;
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
}
 
