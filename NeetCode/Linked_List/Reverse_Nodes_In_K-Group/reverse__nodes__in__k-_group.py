from typing import Optional, List
from common.listnode import ListNode, build_list, print_list

from collections import deque


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy

        count = 0
        for _ in range(k):
            ptr = ptr.next
            if ptr == None:
                break
            count += 1
        if count != k:
            return head

        tmp1, tmp2 = ptr.next, dummy.next

        ptr.next = None
        dummy.next = self.reverseList(dummy.next)
        tmp2.next = self.reverseKGroup(tmp1, k)

        return dummy.next

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
    sol = Solution()

    head = build_list([1, 2, 3, 4, 5, 6])
    k = 3

    print_list(sol.reverseKGroup(head, k))
    print("Running Solution...")
