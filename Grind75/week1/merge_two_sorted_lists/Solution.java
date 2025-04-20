package Grind75.week1.merge_two_sorted_lists;
import common.ListNode;

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode head = new ListNode();
        ListNode tail = head;
        while(list1 != null && list2 != null){
            if(list1.val <= list2.val){
                tail.next = list1;
                list1 = list1.next;
            }else{
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }
        if(list1 != null){
            tail.next = list1;
        }
        else{
            tail.next = list2;
        }

        return head.next;
    }
    
    public static void main(String[] args) {
        System.out.println("Running merge_two_sorted_lists...");
    }
}
