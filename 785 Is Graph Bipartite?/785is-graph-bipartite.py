class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        edges: dict[int, list[int]] = {
            i: x for i, x in enumerate(graph)
        }
        group: list[int] = [-1 for x in range(len(graph))]

        # Keep visitng random nodes
        for node, grp in enumerate(group):
            if grp != -1:
                continue
            
            if not self.visit_node(node, group, edges, 0):
                return False
        
        return True

    def visit_node(self, node: int, group: list[int], edges: dict[int, set[int]], prev_grp: int):
        # Mark this node as 1 - prev group
        group[node] = current_grp = 1 - prev_grp

        # Then keep exploring other nodes
        for edge in edges[node]:
            grp = group[edge]
            if grp == -1:
                if not self.visit_node(edge, group, edges, current_grp):
                    return False
            else:
                if grp != prev_grp:
                    return False

        return True
            