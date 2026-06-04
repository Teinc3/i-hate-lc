# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            curr_node = TreeNode(val=num)
            while stack and curr_node.val > stack[-1].val:
                node = stack.pop()
                curr_node.left = node
            if stack:
                stack[-1].right = curr_node
            stack.append(curr_node)

        return stack[0] if stack else None
            
                

                
        