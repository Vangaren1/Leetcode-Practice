package Grind75.week2.reverse_linked_list_206;
import common.ListNode;

class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null){
            return head;
        } 
        ListNode ptr1 = head;
        ListNode ptr2 = ptr1.next;
        ListNode tmp = head;

        ptr1.next = null;

        while(ptr2 != null){
            tmp = ptr2.next;
            ptr2.next = ptr1;
            ptr1 = ptr2;
            ptr2 = tmp;
        }

        return ptr1;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);

        Solution s = new Solution();

        head = s.reverseList(head);

        System.out.println(head.val);



        System.out.println("Running reverse_linked_list_206...");
    }
}
