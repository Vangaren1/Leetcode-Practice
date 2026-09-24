from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list
from common.treenode import TreeNode, deserialize, printTree, null


class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        # find the middle node
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None

        root = TreeNode(middle.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(middle.next)

        return root


if __name__ == "__main__":
    sol = Solution()
    head = build_list([-10, -3, 0, 5, 9])
    printTree(sol.sortedListToBST(head))
    print("Running Solution...")
