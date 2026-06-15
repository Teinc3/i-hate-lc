# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = p1 = p2 = ListNode(next=head)
        while True:
            p0 = p1
            p1 = p1.next
            if p2:
                p2 = p2.next
                if p2:
                    p2 = p2.next
            if not p2:
                p0.next = p1.next
                break
        
        return i.next