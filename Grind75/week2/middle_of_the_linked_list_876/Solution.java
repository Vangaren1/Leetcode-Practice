package Grind75.week2.middle_of_the_linked_list_876;
import common.ListNode;


class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        if(fast.next == null){
            return slow;
        }else{
            return slow.next;
        }
    }
    public static void main(String[] args) {
        System.out.println("Running middle_of_the_linked_list_876...");
    }
}
