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
        ptr = head
        for i in range(n - 1):
            ptr = ptr.next

        ptr.next = ptr.next.next

        return head


if __name__ == "__main__":
    sol = Solution()
    head = build_list([5])
    n = 1

    print_list(sol.removeNthFromEnd(head, n))
    print("Running Solution...")
