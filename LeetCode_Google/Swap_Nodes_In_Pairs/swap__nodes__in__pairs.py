from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        if head.next is None:
            return head

        n = head.next
        theRest = head.next.next
        n.next = head
        n.next.next = self.swapPairs(theRest)
        return n

        pass


if __name__ == "__main__":
    sol = Solution()
    head = build_list([1, 2, 3, 4])
    print_list(sol.swapPairs(head))
    print("Running Solution...")
