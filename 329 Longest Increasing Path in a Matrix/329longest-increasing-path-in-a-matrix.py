class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_len: int = 0
        dims: tuple[int, int] = [len(matrix), len(matrix[0])]
        scores: dict[tuple[int, int], int] = {
            (row_idx, col_idx): -1
            for row_idx in range(dims[0])
            for col_idx in range(dims[1])
        }

        for col_idx in range(dims[1]):
            for row_idx in range(dims[0]):
                max_len = max(max_len, self.checkCell(
                    row_idx, col_idx, matrix, scores, dims, None
                ))

        return max_len

    def checkCell(
        self, row_idx: int, col_idx: int,
        matrix, scores, dims: [int, int], last_val: int | None
    ) -> int:
        # If this cell does not increase in value - it's not a valid path
        cell_value = matrix[row_idx][col_idx]
        if last_val != None and last_val >= cell_value:
            return 0

        # If this cell already has been explored and has some score already
        # Then return that score
        existing_score = scores[(row_idx, col_idx)]
        if existing_score != -1:
            return existing_score # No +1 because we reuse old cell score

        # Otherwise, we explore this cell
        # Check values of all 4 directions, and recursive if higher
        highest_value = 0

        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # row-offset
            new_idx = (row_idx + y, col_idx + x)
            if (new_idx[0] < 0 or new_idx[0] >= dims[0]
                or new_idx[1] < 0 or new_idx[1] >= dims[1]):
                continue # This path is impossible

            # do a check on this cell!
            highest_value = max(highest_value, self.checkCell(
                new_idx[0], new_idx[1], matrix, scores, dims, cell_value
            ))
        
        # Store this cell's value and return the highest value
        # This score contains itself
        scores[(row_idx, col_idx)] = highest_value + 1
        return highest_value + 1
