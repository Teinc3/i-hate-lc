# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        if head == None:
            return head

        # Traverse to left
        # Save node before left as prev_rev
        count = 0
        prev = head = ListNode(next=head)
        prev_rev = None
        nxt = None
        curr = None
        while True:
            curr = prev.next
            count += 1
            if count == left:
                prev_rev = prev
                prev = curr
                break
            prev = curr

        curr = prev.next # curr at left rn
        # Reverse until right (rev_end)
        while True:
            nxt = curr.next
            curr.next = prev
            count += 1

            if right == count:
                break
            
            prev = curr
            curr = nxt

        prev_rev.next.next = nxt
        prev_rev.next = curr

        return head.next
