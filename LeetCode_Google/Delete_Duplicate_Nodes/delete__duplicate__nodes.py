from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
