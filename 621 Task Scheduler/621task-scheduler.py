from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Idea: Take highest frequency task that is available and decrement 1
        # If no suitable tasks, idle
        
        if not tasks:
            return 0
        task_counter = Counter(tasks)
        curr_interval = 0
        available_tasks = [freq for freq in task_counter.values()]
        unavailable_tasks = deque()
        heapq.heapify_max(available_tasks)

        while available_tasks or unavailable_tasks:
            # Take freq
            if available_tasks:
                freq = heapq.heappop_max(available_tasks)
                if freq > 1:
                    unavailable_tasks.append((curr_interval + n + 1, freq - 1,))
            curr_interval += 1

            # Next cycle - move tasks back
            while unavailable_tasks and unavailable_tasks[0][0] <= curr_interval:
                _, freq = unavailable_tasks.popleft()
                heapq.heappush_max(available_tasks, freq)
        
        return curr_interval
