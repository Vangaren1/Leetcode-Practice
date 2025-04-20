from typing import Optional
from common.listnode import ListNode, build_list, print_list

class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                tmp2 = ptr2.next
                ptr2.next = ptr1
                ptr1 = ptr2 
                ptr2 = tmp2
            
            pass
        
        if list1 is None:
            return list2
        if list2 is None: 
            return list1
            
            
        

if __name__ == "__main__":
    print("Running Solution...")
