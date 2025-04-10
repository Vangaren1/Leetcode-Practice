# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        ptr = head
        tmp = None
        while ptr:
            tmp = ListNode(val=ptr.val, next=tmp)
            ptr = ptr.next
        return tmp


obj = Solution()

t = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))

out= obj.reverseList(t)
while out:
    print(out.val)
    out = out.next

        