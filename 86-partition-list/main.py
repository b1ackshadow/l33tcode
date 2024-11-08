from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser = ListNode()
        lesser_head = lesser
        greater = ListNode()
        greater_head = greater

        while head:
            if head.val < x:
                lesser.next = ListNode(head.val)
                lesser = lesser.next
            else:
                greater.next = ListNode(head.val)
                greater = greater.next
            head = head.next
        lesser.next = greater_head.next
        return lesser_head.next
        
sol = Solution()

inp = [1,4,3,2,5,2]; x = 3
inp = [2,1]; x = 2

head = ListNode()
curr = head
for each in inp:
    curr.next = ListNode(each)
    curr = curr.next

res = sol.partition(head.next, x)

while res:
    print(res.val)
    res = res.next

