class Edge:
    def __init__(self, neighbor: str, weight: float):
        self.neighbor = neighbor
        self.weight = weight

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        flattened_variables = [
            x
            for y in equations
            for x in y
        ]
        edges: dict[str, set[Edge]] = {
            var: set()
            for var in flattened_variables
        }
        
        for i, eq in enumerate(equations):
            edges[eq[0]].add(Edge(eq[1], values[i]))
            edges[eq[1]].add(Edge(eq[0], 1/values[i]))

        keys = edges.keys()
        visited: set[str] = set()
        weights: list[float] = [] # May contain non-unique items

        # Now do queries
        output: list[float] = []
        for q in queries:
            if q[0] not in keys or q[1] not in keys:
                output.append(-1.0)
                continue

            # Do a DFS (allowing a stack of paths)
            visited.clear()
            weights.clear()

            if self.exploreVar(q[0], q[1], edges, visited, weights) != None:
                i = 1.0
                for x in weights:
                    i *= x
                output.append(i)
            else:
                output.append(-1.0)
        
        return output

        
    def exploreVar(
        self, curr: str, target: str, edges: dict[str, set[Edge]],
        visited: set[str], weights: list[float]
    ) -> set[float] | None:
        # Check if current is target:
        if curr == target:
            return weights

        visited.add(curr)
        
        # Search all edges
        for edge in edges[curr]:
            if edge.neighbor in visited: # So we don't get into an infinite loop
                continue

            new_weights = self.exploreVar(
                edge.neighbor, target, edges, visited, weights
            )
            if new_weights != None:
                # A path to the target was found; Returned weight sequence
                new_weights.append(edge.weight)
                return new_weights

        # Nothing was found! Return None
        return None
                