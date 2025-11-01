from typing import Optional, List
from common.listnode import ListNode, build_list, print_list


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        toRemove = set(nums)

        while head and head.val in toRemove:
            head = head.next

        ptr = ListNode(val=0, next=head)

        while ptr:
            if ptr.next and ptr.next.val in toRemove:
                ptr.next = ptr.next.next
                continue
            ptr = ptr.next

        return head


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    head = [1, 2, 3, 4, 5, 6]
    head = build_list(head)
    r = sol.modifiedList(nums, head)
    print_list(r)
    print("Running Solution...")
