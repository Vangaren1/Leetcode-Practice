from typing import Optional, List
from common.listnode import ListNode, build_list, print_list


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        ptr = head
        while l1 and l2:
            tmp = l1.val + l2.val + carry
            carry = 1 if tmp > 9 else 0
            ptr.next = ListNode(tmp % 10)
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            tmp = l1.val + carry
            carry = 1 if tmp > 9 else 0
            ptr.next = ListNode(tmp % 10)
            ptr = ptr.next
            l1 = l1.next

        while l2:
            tmp = l2.val + carry
            carry = 1 if tmp > 9 else 0
            ptr.next = ListNode(tmp % 10)
            ptr = ptr.next
            l2 = l2.next

        if carry == 1:
            ptr.next = ListNode(1)

        return head.next


if __name__ == "__main__":
    sol = Solution()
    l1 = build_list([1, 2, 3])
    l2 = build_list([4, 5, 6])

    print_list(sol.addTwoNumbers(l1, l2))
    print("Running Solution...")
