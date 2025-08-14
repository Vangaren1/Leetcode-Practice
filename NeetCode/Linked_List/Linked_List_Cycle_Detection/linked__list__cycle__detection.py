from typing import Optional, List
from common.listnode import ListNode, build_list, print_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastPtr = head
        slowPtr = head

        seen = set()

        while slowPtr.next and fastPtr.next and fastPtr.next.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
