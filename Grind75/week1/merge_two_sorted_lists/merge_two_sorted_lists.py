from common.listnode import ListNode, build_list, print_list
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        else: 
            tail.next = list2 
        
        return head.next 
    
if __name__ == '__main__':
    l1 = build_list([1,2,4])
    l2 = build_list([1,3,4])
    
    s = Solution()
    
    result = s.mergeTwoLists(l1, l2)
    
    print_list(result)