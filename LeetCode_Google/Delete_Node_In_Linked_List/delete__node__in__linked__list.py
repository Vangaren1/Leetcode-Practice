from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ptr = node
        while ptr and ptr.next:
            ptr.val = ptr.next.val
            ptr = ptr.next
        ptr.next = None

        pass


if __name__ == "__main__":
    sol = Solution()
    head = ([4, 5, 1, 9],)
    node = 5
    head = build_list(head)
    ptr = head
    while ptr and ptr.val != node:
        ptr = ptr.next
    print_list(sol.deleteNode(ptr))

    print("Running Solution...")
