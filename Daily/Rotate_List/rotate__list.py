from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        count = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            count += 1
        k = k % count
        nhead, last = head, head
        for _ in range(k):
            last = last.next
        while last.next:
            last = last.next
            nhead = nhead.next
        last.next = head
        newFront = nhead.next
        nhead.next = None
        return newFront


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
