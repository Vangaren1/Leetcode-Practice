from typing import Optional, List
from common.listnode import ListNode, build_list, print_list


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        array = []
        ptr = head
        while ptr:
            array.append(ptr)
            ptr = ptr.next
        newArray = [
            None,
        ] * len(array)
        index = 0
        for i in range(0, len(array), 2):
            newArray[i] = array[index]
            index += 1

        evenOdd = len(array) % 2
        start = len(array) - 1 - evenOdd
        for j in range(start, 0, -2):
            newArray[j] = array[index]
            index += 1

        for k in range(len(array) - 1):
            newArray[k].next = newArray[k + 1]
        newArray[len(array) - 1].next = None

        return newArray[0]
        pass


if __name__ == "__main__":
    sol = Solution()

    list = build_list([2, 4, 6, 8])

    newList = sol.reorderList(list)

    print_list(newList)
    print("Running Solution...")
