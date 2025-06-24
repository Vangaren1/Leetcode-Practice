package Grind75.week6.construct_bst_from_preorder_and_inorder_105;
import common.TreeNode;

import java.util.Arrays;

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if( preorder.length == 0 || inorder.length == 0){
            return null;
        }

        TreeNode root = new TreeNode(preorder[0]);

        int middle = search(inorder, root.val);

        int[] leftPre = Arrays.copyOfRange(preorder, 1, middle + 1);
        int[] leftIn = Arrays.copyOfRange(inorder, 0, middle);
        root.left = buildTree(leftPre , leftIn);

        int[] rightPre;
        int[] rightIn;
        if ( middle + 1 > preorder.length -1){
            rightPre = null;    
        }else{
            rightPre = Arrays.copyOfRange(preorder, middle + 1, preorder.length -1);
        }
        if ( middle + 1 > inorder.length - 1){
            rightIn = null;
        }else{
            rightIn = Arrays.copyOfRange(inorder, middle + 1 , inorder.length -1);    
        }
        
        root.right = buildTree(rightPre, rightIn);

        return root;

    }

    public int search(int[] array, int target) {
        
        for (int i = 0; i < array.length ; i++) {
            if ( array[i] == target) {
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        System.out.println("Running construct_bst_from_preorder_and_inorder_105...");
    }
}
