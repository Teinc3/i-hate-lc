# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        stack_p = stack_q = None
        current_node = root
        seen_nodes = set()

        while stack:
            current_node = stack[-1]
            seen_nodes.add(current_node.val)

            if current_node.val in (p.val, q.val):
                if current_node.val == p.val:
                    stack_p = stack.copy()
                else:
                    stack_q = stack.copy()
                
                if stack_p and stack_q:
                    for i, (p_node, q_node) in enumerate(zip(stack_p, stack_q)):
                        if p_node.val is not q_node.val:
                            return stack_p[i-1]
                    else:
                        return stack_q[-1] if len(stack_q) <= len(stack_p) else stack_p[-1]
                
            if current_node.left and current_node.left.val not in seen_nodes:
                stack.append(current_node.left)
            elif current_node.right and current_node.right.val not in seen_nodes:
                stack.append(current_node.right)
            else:
                stack.pop()
            
            