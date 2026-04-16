class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        row_states = []
        count_mod = 1_000_000_000 + 7

        # Create list objects (this makes sure they are not the same reference)
        for col in range(n):
            row_states.append([0] * k)
        
        for row in range(m):
            for col in range(n):
                val = grid[row][col]

                if col == 0 and row == 0:
                    row_states[0][val % k] = 1
                else:
                    above_state = row_states[col].copy()
                    row_states[col] = [0] * k
                    if col > 0:
                        # Take left value
                        for mod, count in enumerate(row_states[col - 1]):
                            row_states[col][(val + mod) % k] = (row_states[col][(val + mod) % k] + count) % count_mod
                    if row > 0:
                        # Take the value above us (i.e. the copy)
                        for mod, count in enumerate(above_state):
                            row_states[col][(val + mod) % k] = (count + row_states[col][(val + mod) % k]) % count_mod
                
        return row_states[-1][0]