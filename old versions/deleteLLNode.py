# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

obj = Solution()

test = ListNode('a')
test.next = ListNode('b')
test.next.next = ListNode('c')

n = test.next

obj.deleteNode(n)

while test:
    print(test.val)
    test = test.next

        