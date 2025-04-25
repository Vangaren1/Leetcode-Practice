package Grind75.week1.Linked_List_Cycle_141;
import java.util.HashSet;
import java.util.Set;

import common.ListNode;

class Solution {
    public boolean hasCycle_old(ListNode head) {
        Set<ListNode> seen = new HashSet<>();
        while(head != null){
            if(seen.contains(head)){
                return true;
            }
            seen.add(head);
            head = head.next;
        }
        return false;
    }

    public boolean hasCycle(ListNode head){
        ListNode slow = head;
        ListNode fast = head;

        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast){
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("Running Linked_List_Cycle_141...");
    }
}
