class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 1st pass: Identify all 0s. If 1, identify if a number on adjacent,
        # If so, it is number += 1 and add to next_pass array. Otherwise None.
        # Other+ pass: set None values, and add to next_pass array. 
        # Continue until all Nones resolved.

        m = len(mat)
        n = len(mat[0])
        res = []
        next_pass = set()
        curr_val = 1

        for row in range(m):
            res.append([])
            for col in range(n):
                if mat[row][col] == 0:
                    res[-1].append(0)
                else:
                    res[-1].append(float('inf'))
                    next_pass.add((row, col))

        while next_pass:
            tmp_pass = set()
            for r, c in next_pass:
                # Search four sides
                combins = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                min_val = float('inf')
                tmp = []
                for ro, co in combins:
                    row, col = r + ro, c + co
                    if not (0 <= row < m and 0 <= col < n):
                        continue
                    val = res[row][col]
                    if val == curr_val:
                        continue
                    # Get distance
                    min_val = min(min_val, res[row][col])

                    # Add to next_pass
                    if val > curr_val:
                        tmp.append((row, col))

                if min_val == curr_val - 1:
                    # Cast to int
                    res[r][c] = curr_val
                    # Add to next pass
                    tmp_pass.update(tmp)

            next_pass = tmp_pass
            curr_val += 1

        return res