from typing import Optional, List
from common.listnode import ListNode, build_list, print_list

from collections import deque


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dq = deque([])
        newHead = ListNode()
        ptr = head
        newHead.next = ptr
        front = newHead
        while ptr:
            # put k items in the deque and mark the end
            tmp = ptr

            for _ in range(k):
                if tmp:
                    dq.appendleft(tmp)
                    tmp = tmp.next
            # if the dq has enough to flip, mark the start of the next batch and empty the dq
            if len(dq) == k:
                nxt = tmp
                while dq:
                    n = dq.pop()
                    n.next = nxt
                    nxt = n
                # need to point the front to nxt
                front.next = nxt
                # need to update the front to the next front
                for _ in range(k):
                    front = front.next
            ptr = tmp

        return newHead.next


if __name__ == "__main__":
    sol = Solution()

    head = build_list([1, 2, 3, 4, 5, 6])
    k = 3

    print_list(sol.reverseKGroup(head, k))
    print("Running Solution...")
