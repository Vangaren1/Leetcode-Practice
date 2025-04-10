# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        if head is None or head.next is None:
            return True
        while head:
            temp.append(head.val)
            head = head.next
        for i in range(len(temp)//2):
            if temp[i] != temp[-(i+1)]:
                return False
        return True




obj = Solution()
h = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1))))

test = ListNode(val=1)

temp = test.next
for i in [2,3,3,2,1]:
    temp = ListNode(val=i)
    temp = temp.next

print(test.next)
    




obj.isPalindrome(h)