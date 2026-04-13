class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        combinations = []
        state = []

        def solveRow():
            row = len(state)

            for col in range(n):
                # If col in queens
                # Or col = (queen +- rowdiff) % n
                # Then continue
                if col in state or any((
                    col == q + (row - row_idx)
                    or col == q - (row - row_idx)
                ) for row_idx, q in enumerate(state)):
                    continue
                
                # Otherwise, OK 
                # if row < n, solve(n+1)
                # Otherwise save valid combination
                state.append(col)

                if row < n - 1:
                    solveRow()
                else:
                    states_repr = []
                    for q in state:
                        # col dots in front, n-1-col dots at back
                        state_repr = '.' * q + 'Q' + '.' * (n-1-q)
                        states_repr.append(state_repr)
                    combinations.append(states_repr)

                state.pop()

        
        solveRow()
        return combinations