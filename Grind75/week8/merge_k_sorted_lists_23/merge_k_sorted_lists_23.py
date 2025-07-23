from typing import Optional, List
from common.listnode import ListNode, build_list, print_list

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        hq = []

        if len(lists) == 0:
            return hq

        for list in lists:
            ptr = list
            while ptr:
                heapq.heappush(hq, ptr.val)
                ptr = ptr.next

        if hq:
            head = ListNode(heapq.heappop(hq))
        else:
            head = None
        ptr = head
        while hq:
            ptr.next = ListNode(heapq.heappop(hq))
            ptr = ptr.next

        return head


if __name__ == "__main__":
    s = Solution()

    l1 = build_list([1, 4, 5])
    l2 = build_list([1, 3, 4])
    l3 = build_list([2, 6])
    lists = [l1, l2, l3]

    print(s.mergeKLists(lists))
    print("Running Solution...")
