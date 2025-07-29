package Grind75.week8.serialize_and_deserialize_bst_297;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Queue;

import common.TreeNode;

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        String tmp = "";
        if (root == null)
            return tmp;

        List<TreeNode> que = new ArrayList<>();
        que.add(root);

        while (!que.isEmpty()) {
            TreeNode curr = que.remove(que.size() - 1);
            if (curr == null) {
                tmp = tmp + "/N";
            } else {
                tmp = tmp + "/" + Integer.toString(curr.val);
                que.add(0, curr.left);
                que.add(0, curr.right);
            }
        }

        return tmp;

    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.length() == 0)
            return null;

        String[] s = data.split("/");
        List<String> array = new ArrayList<>(Arrays.asList(s));

        array.remove(0);

        List<TreeNode> nodes = new ArrayList<>();
        for (String tmp : array) {
            if (tmp.compareTo("N") == 0) {
                nodes.add(null);
            } else {
                int val = Integer.parseInt(tmp);
                nodes.add(new TreeNode(val));
            }
        }

        List<TreeNode> child = new ArrayList<>(nodes);
        Collections.reverse(child);

        TreeNode root = child.remove(child.size() - 1);

        for (TreeNode t : nodes) {
            if (t != null) {
                if (child.size() > 0)
                    t.left = child.remove(child.size() - 1);
                if (child.size() > 0)
                    t.right = child.remove(child.size() - 1);
            }
        }
        return root;
    }

    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>(Arrays.asList(1, 2, 3, null, null, 4, 5));

        TreeNode root = common.TreeNode.deserialize(nums);

        Codec c = new Codec();

        String ser = c.serialize(root);
        System.out.println(ser);
        TreeNode r = c.deserialize(ser);

        System.out.println("Running serialize_and_deserialize_bst_297...");
    }
}
