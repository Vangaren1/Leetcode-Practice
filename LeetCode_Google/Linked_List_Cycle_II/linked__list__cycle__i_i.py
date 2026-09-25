from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()

        ptr = head

        while ptr:
            if ptr in seen:
                return ptr
            seen.add(ptr)
            ptr = ptr.next

        return None


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")
