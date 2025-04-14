from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Val = self.convertFromList(l1)
        l2Val = self.convertFromList(l2)
        rVal = l1Val + l2Val 
        resultValue =  self.convertToList(rVal)
        return resultValue
        

    def convertFromList(self, l1: Optional[ListNode]) -> int:
        result = 0
        tens = 0
        while l1:
            result += l1.val * 10**tens
            tens += 1
            l1 = l1.next
        return result

    def convertToList(self, num: int) -> Optional[ListNode]:
        start = ListNode(val = num % 10 )
        num -= num % 10 
        num = num // 10
        ptr = start
        while num > 0:
            ptr.next = ListNode(val = num % 10 )
            num -= num % 10
            num = num // 10
            ptr = ptr.next
        return start 
    
    
s = Solution()

l1 = ListNode(2, next=ListNode(4, next=ListNode(3)))
l2 = ListNode(5, next=ListNode(6, next=ListNode(4)))

s.addTwoNumbers(l1, l2)