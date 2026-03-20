"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes: dict[int, Node] = {}

        # BFS explore all nodes
        self.checkAddNode(nodes, node)
        return nodes[node.val]
    
    def checkAddNode(self, nodes: dict[int, Node], old_node: Node):
        # If node exists, then quit (as its neighbors have already been searched)
        if old_node.val in nodes:
            return

        # If node doesn't exist, create it, and continue with neighbors
        new_node = Node(old_node.val)
        nodes[old_node.val] = new_node
        for nb_node in old_node.neighbors:
            self.checkAddNode(nodes, nb_node)
            new_node.neighbors.append(nodes[nb_node.val])
        