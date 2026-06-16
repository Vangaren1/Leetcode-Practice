from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nh = ListNode(0, next=head)
        slow, fast = nh, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    sol = Solution()
    head = build_list([1, 3, 4, 7, 1, 2, 6])
    print_list(sol.deleteMiddle(head))
    print("Running Solution...")
