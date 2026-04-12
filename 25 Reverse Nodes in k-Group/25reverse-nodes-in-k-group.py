# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        # First declare a dummy node that points to head.
        head = p1 = p7 = ListNode(next=head)

        # Now start looping.
        while True:
            # 1. Traverse k steps from dummy node
            steps = 0
            p2 = p1
            while steps < k:
                p2 = p2.next
                # If we exhaust the remaining nodes, the list is reversed
                if p2 is None:
                    return head.next
                steps += 1
            
            # Now p2 is at the last element to be reversed in the group (k)
            # 2. Declare p3 to be next element of p2, i.e. start of NEXT group.
            p3 = p2.next 
            # 3. Set p4, p7 to next of p1
            p4 = p7 = p1.next
            # 4. Wire the last element of the last k-group (or dummy node)
            # to the current k-group's LAST element (which will be reversed)
            p1.next = p2
            
            # 5. Declare p5 to the next element of p4
            p5 = p4.next
            # Now we loop until the conditions are broken
            while True:
                # 1. Save the next node pointed by p5
                p6 = p5.next
                # 2. Reverse the pointer (p4->p5 becomes p4<-p5)
                p5.next = p4
                # Check: Is this already the last node in the k-group?
                if p5 is p2:
                    # Yes - quit the loop
                    break
                # otherwise, swap variables and move on to the next node
                p4 = p5
                p5 = p6

            # 6. Now we move on to the next k-group
            # Link the first element (now last) of the k-group to the next
            p7.next = p3
            # Set p1 as the LAST element preceeding the next k-group
            # The other variables will be redeclared, so no need to wipe them.
            p1 = p7 # p7 = p1.next (start of k-group, swapped to become the end)