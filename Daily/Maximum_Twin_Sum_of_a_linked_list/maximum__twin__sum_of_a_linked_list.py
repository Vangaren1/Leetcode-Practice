from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = self.reverseList(slow)

        first = head
        curr = 0

        while second:
            curr = max(curr, first.val + second.val)
            first = first.next
            second = second.next

        return curr

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
    print("Running Solution...")
