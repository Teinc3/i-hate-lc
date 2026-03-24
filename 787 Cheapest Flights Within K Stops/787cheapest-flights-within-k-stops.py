import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges: dict[int, list[tuple[int, int]]] = {
            x: list() for x in range(n)
        }

        for flight in flights:
            fro, to, price = flight
            edges[fro].append((to, price))

        # Total price | steps | node
        heap = [(0, 0, src)]
        heapq.heapify(heap)
        # node -> list of (prices, steps)
        visited: dict[int, list[tuple[int, int]]] = {
            x: list() for x in range(n)
        }

        cheapest_price: int = -1

        while heap:
            price, steps, node = heapq.heappop(heap)

            # If this is the destination node then set cheapest_price
            if node == dst:
                cheapest_price = price if cheapest_price == -1 else min(cheapest_price, price)
                continue

            # Or if we have exhausted all steps already, return early
            if steps > k:
                continue

            # For this number of steps or lower
            # If there's a lower price
            # We skip this combination
            if any([x[0] <= price and x[1] <= steps for x in visited[node]]):
                continue
            else:
                visited[node].append((price, steps))
            
            # Explore all other nodes and add them to the heap
            for edge in edges[node]:
                heapq.heappush(heap, (price + edge[1], steps + 1, edge[0]))
        
        return cheapest_price