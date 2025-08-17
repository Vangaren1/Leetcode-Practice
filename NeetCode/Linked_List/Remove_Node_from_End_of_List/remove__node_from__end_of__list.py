from typing import Optional, List
from common.listnode import ListNode, build_list, print_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # find the length
        count = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            count += 1

        if count == n:
            return head.next

        # go to the node before the nth node
        ptr = ListNode()
        ptr.next = head
        for i in range(count - n):
            ptr = ptr.next

        if ptr and ptr.next:
            ptr.next = ptr.next.next

        return head


if __name__ == "__main__":
    sol = Solution()
    head = build_list([1, 2])
    n = 2

    print_list(sol.removeNthFromEnd(head, n))
    print("Running Solution...")
