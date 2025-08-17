from typing import Optional, List
from common.listnode import ListNode, build_list, print_list


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newHead = ListNode()

        ptr = newHead

        while lists:
            listPtr = None
            index = -1
            for idx, lst in enumerate(lists):
                if lst is None:
                    continue
                # grab the list with the lowest value
                if listPtr is None or lst.val < listPtr.val:
                    index = idx
                    listPtr = lst
            if index == -1:
                lists.pop()
                continue
            # point the head towards that
            if listPtr:
                ptr.next = listPtr
            # increment the listPtr to the next value (or none)
            if index >= 0:
                lists[index] = lists[index].next
            # if its the last, remove it from the list
            if lists[index] == None:
                lists.pop(index)
                index = -1
            ptr = ptr.next

        return newHead.next


if __name__ == "__main__":
    sol = Solution()

    lists = [[], []]
    lists = [build_list(l) for l in lists]

    print_list(sol.mergeKLists(lists))
    print("Running Solution...")
