from typing import Optional, List
from common.listnode import ListNode, build_list, print_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ptrfirst = head
        ptrSecond = ListNode(None)
        ptrSecond.next = head
        count = 0
        start = False
        while ptrfirst:
            ptrfirst = ptrfirst.next
            if start:
                ptrSecond = ptrSecond.next
            count += 1
            if count == n:
                start = True

        if ptrSecond and ptrSecond.next:
            ptrSecond.next = ptrSecond.next.next

        if count == 1:
            return ptrSecond.next

        if count == n:
            return head.next

        return head


if __name__ == "__main__":
    sol = Solution()

    head = [1, 2, 3, 4, 5]

    head = build_list(head)

    # print_list(sol.removeNthFromEnd(head, 2))
    # print_list(sol.removeNthFromEnd(build_list([1]), 1))
    print_list(sol.removeNthFromEnd(build_list([1, 2]), 2))
    print("Running Solution...")
