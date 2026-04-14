class Solution:
    def totalNQueens(self, n: int) -> int:
        global combinations
        global col_mask
        global diag_mask_1
        global diag_mask_2

        combinations = 0
        col_mask = 0
        diag_mask_1 = 0
        diag_mask_2 = 0

        def solveRow(row = 0):
            global combinations
            global col_mask
            global diag_mask_1
            global diag_mask_2
            
            # Iterate only to first half (inclusive of median)
            for col in range((n+1)//2 if row == 0 else n):
                col_bit = 1 << col
                diag_1_bit = 1 << (row - col + n - 1)
                diag_2_bit = 1 << (row + col)
                # If col in queens
                # Or col = (queen +- rowdiff) % n
                # Then continue
                if (
                    col_mask & col_bit
                    or diag_mask_1 & diag_1_bit 
                    or diag_mask_2 & diag_2_bit
                ):
                    continue
                
                # Otherwise, OK 
                # if row < n, solve(n+1)
                # Otherwise add valid combination
                if row < n - 1:
                    col_mask |= col_bit
                    diag_mask_1 |= diag_1_bit
                    diag_mask_2 |= diag_2_bit
                    solveRow(row + 1)
                else:
                    combinations += 1

                col_mask &= ~col_bit
                diag_mask_1 &= ~diag_1_bit
                diag_mask_2 &= ~diag_2_bit

                # If this is the end of the first half (not including median)
                # Double the combinations (mirrored)
                if row == 0 and col == n//2 - 1: # 5//2 - 1 = 1, 6//2 - 1 = 2
                    combinations *= 2
        
        solveRow()
        return combinations