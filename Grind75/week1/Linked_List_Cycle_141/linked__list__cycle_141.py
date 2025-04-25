from typing import Optional
from common.listnode import ListNode, build_list, print_list

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        ptr = head
        while ptr:
            if ptr in seen: 
                return True
            seen.add(ptr)
            ptr = ptr.next
        return False


if __name__ == "__main__":
    print("Running Solution...")
