package Grind75.week3.binary_tree_level_order_traversal;

import common.TreeNode;

import java.util.ArrayList;
import java.util.List;

class Solution {    
    List<List<Integer>> results = new ArrayList<>();

    public List<List<Integer>> levelOrder(TreeNode root) {
        traverse(root, 0);
        return results;
    }

    public void traverse(TreeNode node, int level){
        if(node != null){
            if( results.size() < (level + 1)){
                results.add(new ArrayList<>());
            }
            results.get(level).add(node.val);
            traverse(node.left, level + 1);
            traverse(node.right, level + 1);
        }
    }
    public static void main(String[] args) {
        System.out.println("Running binary_tree_level_order_traversal...");
    }
}
