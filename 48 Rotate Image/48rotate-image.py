from math import ceil

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        mid = n/2
        for r in range(ceil(mid)): # Rounds up the .5 if exists
            for c in range(int(mid)): # Removes up the .5 if exists
                # <r, c> -> <c, (n - r - 1)>
                matrix[c][n - r - 1], matrix[n - r - 1][n - c - 1], matrix[n - c - 1][r], matrix[r][c] = matrix[r][c], matrix[c][n - r - 1], matrix[n - r - 1][n - c - 1], matrix[n - c - 1][r]
