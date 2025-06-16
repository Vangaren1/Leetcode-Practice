package Grind75.week6.binary_tree_right_side_view_199;
import java.util.ArrayList;
import java.util.List;

import common.TreeNode;

class Solution {

    List<List<Integer>> results = new ArrayList<>();


    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> rSideResults = new ArrayList<>();

        traverse(root, 0);

        for (List<Integer> tmp : results){
            rSideResults.add( tmp.get( tmp.size() -1));
        }

        return rSideResults;
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
        System.out.println("Running binary_tree_right_side_view_199...");
    }
}
