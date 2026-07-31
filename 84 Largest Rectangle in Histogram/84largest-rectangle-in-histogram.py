class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # If it decreases, pop everything and calculate max
        stack = []
        largest = 0
        heights.append(0) # end
        idx = None

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                idx = stack.pop()
                # Calculate the max height
                pse_idx = stack[-1] if stack else -1
                largest = max(largest, heights[idx] * (i - pse_idx - 1))
            stack.append(i)
        
        return largest
        