package Extra.intersection_of_two_linked_lists_160;
import java.util.HashSet;
import java.util.Set;

import common.ListNode;

class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode ptr1 = headA;
        ListNode ptr2 = headB;
        Set<ListNode> seen = new HashSet<>();
        while (ptr1 != null){
            seen.add(ptr1);
            ptr1 = ptr1.next;
        }
        while ( ptr2 != null){
            if ( seen.contains(ptr2)) return ptr2;
            ptr2 = ptr2.next;
        }
        return null;
    }
    public static void main(String[] args) {

        System.out.println("Running intersection_of_two_linked_lists_160...");
    }
}
