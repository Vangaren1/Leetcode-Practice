# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        if head is None:
            return None
        if head.val == val:
            return self.removeElements(head.next, val)
        if head.next:
            n = self.removeElements(head.next, val)
            head.next = n
            return head
        return head




a = ListNode(val=2)
b = ListNode(val=3)
c = ListNode(val=3)
d = ListNode(val=5)
a.next=b
b.next=c
c.next=d

head = a 


obj=Solution()
obj.removeElements(head, 3)
        
print(head.val)
print(head.next.val)