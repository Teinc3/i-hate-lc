# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        tree_nodes: dict[tuple[int, int], TreeNode] = {}

        def generateTree(start: int, end: int):
            if start == end:
                return [TreeNode(start)]
            elif start > end:
                return [None]

            rng = (start, end)
            if rng in tree_nodes:
                return tree_nodes[rng]
            else:
                tree_nodes[rng] = []

            for root in range(start, end + 1):
                left_trees = generateTree(start, root - 1)
                right_trees = generateTree(root + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        node = TreeNode(root, left_tree, right_tree)
                        tree_nodes[rng].append(node)
            
            return tree_nodes[rng]

        return generateTree(1, n)