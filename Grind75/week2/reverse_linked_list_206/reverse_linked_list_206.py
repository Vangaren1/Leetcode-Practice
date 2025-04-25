from typing import Optional
from common.listnode import ListNode, build_list, print_list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        ptr1 = head
        ptr2 = ptr1.next
        ptr1.next = None
        while ptr2:
            tmp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = tmp
        
        return ptr1            
            

if __name__ == "__main__":
    
    l = build_list([i for i in range(10)])
    s = Solution()
    res = s.reverseList(l)
    
    print_list(res)
    print("Running Solution...")
