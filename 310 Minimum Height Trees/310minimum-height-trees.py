from collections import deque 

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        nodes: dict[int, list[int]] = {
            x: list() for x in range(n)
        }

        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])

        neighbours = set()
        h = 0
        while True:
            # If there are less than 2 nodes return
            if n <= 2:
                return list(neighbours)

            # Find all nodes with only 1 connection
            # First time only
            # We can reuse neighbor information later
            single_nodes = [
                node for node in (nodes.keys() if h == 0 else neighbours)
                if len(nodes[node]) == 1
            ]
            
            neighbours.clear()

            # Delete the nodes
            # And remove the neighbors' "neighbor" reference of this node 
            for s_nd in single_nodes:
                nb = nodes[s_nd].pop()
                nodes[nb].remove(s_nd)
                # Store this nb node for next round, we'll want it
                neighbours.add(nb)
                n -= 1

            # Bump height
            h += 1