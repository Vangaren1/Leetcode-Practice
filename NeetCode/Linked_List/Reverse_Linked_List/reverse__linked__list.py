from typing import Optional, List
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
    sol = Solution()
    head = [0, 1, 2, 3]
    head = build_list(head)

    print_list(sol.reverseList(head))
    print("Running Solution...")
