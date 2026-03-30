# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            for i in range(0, len(lists), 2):
                # Merge i and i+1, and put it into i // 2
                lists[i//2] = self.merge2Lists(
                    lists[i], lists[i+1] if len(lists) > i + 1 else None
                )
            del lists[(len(lists)+1)//2:]
        
        return lists[0] if lists else None

    def merge2Lists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        start_node = curr_node = None

        while list1 or list2:
            use_list: int = 0

            if list1 and list2:
                use_list = 1 if list1.val <= list2.val else 2
            else:
                use_list = 1 if list1 else 2

            tmp_node = list1 if use_list == 1 else list2
            if use_list == 1:
                list1 = list1.next
            else:
                list2 = list2.next

            if not start_node:
                start_node = tmp_node
            if curr_node:
                curr_node.next = tmp_node
            curr_node = tmp_node

        return start_node
