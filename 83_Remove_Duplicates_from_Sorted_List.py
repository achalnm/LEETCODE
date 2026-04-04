class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1, ListNode(1, ListNode(2)))

curr = head

while curr and curr.next:
    if curr.val == curr.next.val:
        curr.next = curr.next.next
    else:
        curr = curr.next

res = []
curr = head
while curr:
    res.append(curr.val)
    curr = curr.next

print(res)