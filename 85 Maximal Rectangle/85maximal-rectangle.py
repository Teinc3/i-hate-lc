class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * (len(matrix[0]) + 1) # for autopop resolvement
        stack = []
        area = 0
        for row in matrix:
            row.append("0")
            for i, col in enumerate(row):
                heights[i] = heights[i] + 1 if col == "1" else 0

                while stack and heights[stack[-1]] > heights[i]:
                    idx = stack.pop()
                    prev_idx = stack[-1] if stack else -1
                    area = max(area, heights[idx] * (i - prev_idx - 1))
                # Pop the final
                stack.append(i)
            
            stack.clear() # clean the stack
        
        return area