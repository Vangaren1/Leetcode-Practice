package Grind75.week8.merge_k_sorted_lists_23;

import java.util.PriorityQueue;

import common.ListNode;

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        if (lists.length == 0)
            return null;

        for (ListNode list : lists) {
            ListNode ptr = list;
            while (ptr != null) {
                pq.add(ptr.val);
                ptr = ptr.next;
            }
        }

        if (pq.size() == 0) {
            return null;
        }

        ListNode head = new ListNode(pq.poll());
        ListNode ptr = head;
        while (pq.size() > 0) {
            ptr.next = new ListNode(pq.poll());
            ptr = ptr.next;
        }

        return head;

    }

    public static void main(String[] args) {
        System.out.println("Running merge_k_sorted_lists_23...");
    }
}
