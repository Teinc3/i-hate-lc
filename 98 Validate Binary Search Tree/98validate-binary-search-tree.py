# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [root]
        directions = []

        while stack:    
            curr = stack[-1]
            nxt = None
            is_left = None   

            if curr.left:
                is_left = True
                nxt = curr.left                    
                curr.left = None # Remove this dependency
            
            elif curr.right:
                is_left = False
                nxt = curr.right
                curr.right = None
            
            else:
                # This node has no more children to inspect, remove it
                stack.pop()
                if directions:
                    directions.pop()
                continue
            
            directions.append((curr.val, is_left))
            if any((nxt.val >= val
                    if is_left
                    else nxt.val <= val
                ) for val, is_left in directions):
                return False
            stack.append(nxt)

        return True
            