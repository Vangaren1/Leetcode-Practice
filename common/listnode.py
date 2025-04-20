
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def build_list(values):
    head = ListNode(0)
    curr = head
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return head.next

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")