# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll_final = ll = ListNode()
        overflow = 0
        while l1 and l1.val != None or l2 and l2.val != None:
            v1 = l1.val if l1 and l1.val != None else 0
            v2 = l2.val if l2 and l2.val != None else 0
            res = v1 + v2 + overflow
            overflow = res // 10
            mod = res % 10
            ll.next = ListNode(mod, None)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            ll = ll.next

        if overflow == 1:
            ll.next = ListNode(1, None)

        return ll_final.next