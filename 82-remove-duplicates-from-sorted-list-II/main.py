from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-300, head)
        last_unique = dummy
        prev = dummy
        while head:
            print(f"{head.val}")
            print(f"next = {head.next.val if head.next else None}")
            if  prev.val != head.val and (not head.next or head.next.val != head.val):
                # unique node
                last_unique.next = head
                last_unique = head

            prev = head
            head = head.next
        return dummy.next

sol = Solution()

head = ListNode()
dummy = head
case1 = [1,2,3,3,4,4,5]
case2 = [1,1,1,2,3]
for each in case2:
    dummy.next = ListNode(each)
    dummy = dummy.next


res = sol.deleteDuplicates(head.next)

while res:
    print(res.val)
    res = res.next

