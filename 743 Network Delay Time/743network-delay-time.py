import heapq

class Edge:
    def __init__(self, target: int, time: int):
        self.target = target
        self.time = time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges: dict[int, set[Edge]] = {
            x: set() for x in range(1, n+1)
        }
        heap = [(0, k)]
        heapq.heapify(heap)

        for time in times:
            source, target, time = time
            edges[source].add(Edge(target, time))
        
        visited: set[int] = set()
        current_node = 0
        time = 0

        while len(visited) < n:
            # Pop a tuple from the heap and push 
            try:
                tmp_time, current_node = heapq.heappop(heap)
                if current_node in visited:
                    continue
                time = tmp_time
                visited.add(current_node)
            except IndexError:
                # Check if we have visited all nodes
                # If yes, then this one is the final, return it
                # If no, then return -1
                return time if len(visited) == n else -1
            
            # Explore all adjacent nodes
            for edge in edges[current_node]:
                # Push if not in visited
                if edge.target not in visited:
                    heapq.heappush(heap, (edge.time + time, edge.target))        

        return time