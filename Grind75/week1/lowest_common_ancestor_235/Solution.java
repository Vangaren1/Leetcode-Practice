package Grind75.week1.lowest_common_ancestor_235;
import common.TreeNode;

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        TreeNode ptr = new TreeNode();
        while(ptr != null){
            if(ptr.val > p.val && ptr.val > q.val){
                ptr = ptr.left;
            }else if(ptr.val < p.val && ptr.val < q.val){
                ptr = ptr.right;
            }else{
                return ptr;
            }
        }

        return ptr;
    }

    public static void main(String[] args) {
        System.out.println("Running lowest_common_ancestor_235...");
    }
}
