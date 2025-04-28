from typing import Optional
from common.listnode import ListNode, build_list

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if(fast.next is None):
            return slow
        else:
            return slow.next
    
    
    
if __name__ == "__main__":
    
    root = [ i for i in range(1,7)]
    root = build_list(root)
    
    s = Solution()
    result = s.middleNode(root)
    print(result.val)
    
    print("Running Solution...")
