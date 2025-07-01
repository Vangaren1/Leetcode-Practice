from typing import Optional, List
from common.listnode import ListNode, build_list, print_list

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        ptr1 = headA
        ptr2 = headB
        while ptr1 and ptr2:
            if ptr1 in seen:
                return ptr1
            if ptr2 in seen:
                return ptr2
            seen.add(ptr1)
            seen.add(ptr2)
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return None
                
        
        pass 

if __name__ == "__main__":
    print("Running Solution...")
