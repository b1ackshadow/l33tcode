from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def reverseLL(self, head):
        curr = head
        new_head = None

        while curr:
            next = curr.next
            curr.next = new_head
            new_head = curr
            curr = next
        return new_head
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next or not head.next.next:
            return

        slow = head
        fast = head
        

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second partition
        head2 = self.reverseLL(slow.next)
        curr = head

        slow.next = None
        while  curr != slow.next and head2:

            temp = curr.next
            curr.next = head2

            head2 = head2.next
            curr.next.next = temp
            curr = temp
        return 
        

head = ListNode()
curr = head

# inp = [1,2,3,4]
inp = [1,2,3,4, 5]

for each in inp:
    curr.next = ListNode(each)
    curr = curr.next

sol = Solution()
sol.reorderList(head.next)

res = head.next
while res:
    print(res.val)
    res = res.next



