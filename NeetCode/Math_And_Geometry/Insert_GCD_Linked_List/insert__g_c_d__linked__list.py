from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list
import math


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:

        ptr = head

        while ptr and ptr.next:
            g = math.gcd(ptr.val, ptr.next.val)
            tmp = ptr.next
            ptr.next = ListNode(g, next=tmp)
            ptr = ptr.next.next

        return head

        pass


if __name__ == "__main__":
    sol = Solution()
    head = [18, 6, 10, 3]
    head = build_list(head)
    print_list(sol.insertGreatestCommonDivisors(head))
    print("Running Solution...")
