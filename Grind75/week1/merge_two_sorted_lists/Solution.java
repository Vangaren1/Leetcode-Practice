package Grind75.week1.merge_two_sorted_lists;
import common.ListNode;

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode ptr1 = list1;
        ListNode ptr2 = list2;
        ListNode tmp;
        while(ptr1 != null && ptr2 != null){
            if(ptr1.val <= ptr2.val){
                tmp = ptr2.next;
                ptr2.next = ptr1;
                ptr2 = tmp;
            }else{
                ptr1 = ptr1.next;
            }
        }
        

        return list1;
    }
    

    public static void main(String[] args) {
        System.out.println("Running merge_two_sorted_lists...");
    }
}
