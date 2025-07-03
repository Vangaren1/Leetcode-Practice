package Extra.remove_linked_list_elements_208;

import common.ListNode;

class Solution {
    public ListNode removeElements(ListNode head, int val) {
        while ( head != null && head.val == val){
            head = head.next;
        }
        
        ListNode ptr = head;
        
        while ( ptr != null) {
            if (ptr.next != null && ptr.next.val == val){
                ptr.next = ptr.next.next;
            }else{
                ptr = ptr.next;
            }
            
        }
        return head;
    }
    public static void main(String[] args) {
        System.out.println("Running remove_linked_list_elements_208...");
    }
}
