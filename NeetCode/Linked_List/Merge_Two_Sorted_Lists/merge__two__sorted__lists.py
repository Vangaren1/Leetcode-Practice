from typing import Optional, List
from common.listnode import ListNode, build_list, print_list


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        newHead = ListNode()

        ptr = newHead
        while list1 and list2:
            if list1.val <= list2.val:
                tmp = list1
                list1 = list1.next
            else:
                tmp = list2
                list2 = list2.next
            tmp.next = None
            ptr.next = tmp
            ptr = ptr.next

        if list1:
            ptr.next = list1

        if list2:
            ptr.next = list2

        return newHead.next


if __name__ == "__main__":
    sol = Solution()
    list1 = build_list([1, 2, 4])
    list2 = build_list([1, 3, 5])

    print_list(sol.mergeTwoLists(list1, list2))
    print("Running Solution...")
