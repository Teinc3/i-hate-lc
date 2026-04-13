class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Construct array
        arr = [-1] * (max([interval[1] for interval in intervals]) + 1)
        for x in intervals:
            arr[x[0]] = max(arr[x[0]], x[1])
        
        merged_intervals = []
        current_interval = [-1, -1]
        for i, val in enumerate(arr):
            if current_interval[0] == -1 and val != -1:
                # Start new interval
                current_interval[0] = i

            if val > current_interval[1]:
                # Extend the end
                current_interval[1] = val

            if current_interval[1] == i:
                # Complete this interval
                merged_intervals.append(current_interval.copy())
                current_interval[0] = -1

        return merged_intervals