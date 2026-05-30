# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Edge case N=0
        if head == None:
            return head
        
        # Traverse down list to find the first number gte x
        dummy_head = p_fl_old = ListNode(next=head) # At dummy node
        p_fl = None

        while True:
            p_fl = p_fl_old.next
            if p_fl is None:
                # Traversed the entire list, no nodes need to be swapped
                return dummy_head.next
            elif p_fl.val >= x:
                # Where the p_fl pointer should be placed at
                break
            p_fl_old = p_fl
        
        # Now traverse down from p_fl and move everything over
        p_st_old = p_fl
        p_st = None
        while True:
            p_st = p_st_old.next
            if p_st is None:
                return dummy_head.next # Again, nth to swap as we reached the end

            elif p_st.val < x:
                # Do the swap
                p_st_nxt = p_st.next
                p_st_old.next = p_st_nxt
                p_st.next = p_fl
                p_fl_old.next = p_st
            
                p_fl_old = p_st
                p_st = p_st_nxt
            
            else:
                p_st_old = p_st
        
        return dummy_head.next
