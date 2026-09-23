from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        count = defaultdict(int)
        ptr = head
        while ptr:
            count[ptr.val] += 1
            ptr = ptr.next

        dummy = ListNode()
        dummy.next = head

        ptr = dummy
        while ptr:
            if ptr.next:
                if count[ptr.next.val] > 1:
                    ptr.next = ptr.next.next
                    continue
            ptr = ptr.next

        return dummy.next
        pass


if __name__ == "__main__":
    sol = Solution()
    head = [1, 2, 3, 3, 4, 4, 5]
    head = build_list(head)
    print_list(sol.deleteDuplicates(head))
    print("Running Solution...")
