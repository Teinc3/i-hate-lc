class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row_idx in range(9):
            for col_idx in range(9):
                cell_val = board[row_idx][col_idx]
                if cell_val == ".":
                    continue
                
                # Row/Col check
                for idx in range(9):
                    if (cell_val == board[idx][col_idx] and idx != row_idx
                        or cell_val == board[row_idx][idx] and idx != col_idx):
                        return False
                
                # Box check
                box_row_idx = row_idx // 3
                box_col_idx = col_idx // 3
                for r in range(3 * box_row_idx, 3 * (box_row_idx + 1)):
                    for c in range(3 * box_col_idx, 3 * (box_col_idx + 1)):
                        if (cell_val == board[r][c]
                            and r != row_idx and c != col_idx):
                            return False
                
        return True