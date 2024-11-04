from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # find len of LL so that we can k%n to potentially reduce
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        k = k % n

        # now use slow pointer to find the n-k th node and we need to attach this to head
        slow = head
        fast = head
        i = 0
        while fast and fast.next and i < k:
            fast = fast.next
            i += 1

        # at this point fast is 'k' steps ahead of slow. when fast hits the last node slow will be at n-k
        while fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None
        return head

sol = Solution()

head = [1,2,3,4,5]; k = 2
head = [0,1,2]; k = 4

dummy = ListNode()
curr = dummy
for each in head:
    curr.next = ListNode(each)
    curr = curr.next
res = sol.rotateRight(dummy.next, k)

curr = res

while curr:
    print(curr.val)
    curr = curr.next


