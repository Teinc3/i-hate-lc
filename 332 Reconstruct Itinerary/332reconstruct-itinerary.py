class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges: dict[int, list[str]] = {}

        for src, dst in tickets:
            if src in edges:
                edges[src].append(dst)
            else:
                edges[src] = [dst]
            
            if dst not in edges:
                edges[dst] = []
        
        # Sort outdegree by reverse so efficient popping can be done
        for edge in edges.values():
            edge.sort(reverse=True)

        # Start at JFK
        itinerary: list[str] = []
        self.navigateNode("JFK", edges, itinerary, len(tickets))

        return list(reversed(itinerary))

    def navigateNode(
        self, node_key: str, edges: dict[int, Node], 
        itinerary: list[str], len_tickets: int
    ) -> bool:
        # Check all outbound nodes:
        outdegrees = edges[node_key]
        while len(outdegrees) > 0:
            # First pop this possible flight
            next_node_key = outdegrees.pop()

            # Then traverse it.
            if self.navigateNode(
                next_node_key, edges, itinerary, len_tickets
            ):
                return True

            # Because traverse failed, it will continue to look at the next edge

        # We iterated all edges and failed, so this is not an error on our end.
        # This must be one of the last nodes.
        # We let the node earlier than us try.
        itinerary.append(node_key)
        return False
