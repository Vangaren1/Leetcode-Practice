

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if head is None:
            return False
        visited = {}
        ptr = head
        while True:
            if ptr in visited.keys():
                return True
            if ptr.next == None:
                return False
            visited[ptr]=True
            ptr = ptr.next




test = [1,2,3]

head = ListNode(0)
ptr = head
for t in test:
    temp = ListNode(t)
    ptr.next = temp
    ptr = temp


p = head
while p:
    print(p.val)
    p = p.next
