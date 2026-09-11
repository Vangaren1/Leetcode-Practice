from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        left = head

        left = self.sortList(left)
        right = self.sortList(right)

        dummy = ListNode()
        ptr = dummy

        while left and right:
            if left.val < right.val:
                ptr.next = left
                left = left.next
            else:
                ptr.next = right
                right = right.next
            ptr = ptr.next

        ptr.next = left if left else right

        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 19, 14, 5, -3, 1, 8, 5, 11, 15]
    head = build_list(nums)
    print_list(sol.sortList(head))
    print("Running Solution...")


""" 
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hq = []

        ptr = head
        count = 0
        while ptr:
            heapq.heappush(hq, (ptr.val, count, ptr))
            count += 1
            ptr = ptr.next

        dummyHead = ListNode(val=-1)
        ptr = dummyHead
        while hq:
            _, _, tmp = heapq.heappop(hq)
            ptr.next = tmp
            ptr = ptr.next
        if ptr:
            ptr.next = None
        return dummyHead.next
"""
