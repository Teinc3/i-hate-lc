import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cycle = numRows + max(0, numRows - 2)
        len_s = len(s)
        row_count = math.ceil(len_s/cycle)
        output = ""

        for curr_row in range(numRows):
            j = 0
            while j < len_s:
                try:
                    output += s[j + curr_row]
                    if curr_row == 0 or curr_row == numRows - 1:
                        pass
                    else:
                        output += s[j + cycle - curr_row]
                except IndexError:
                    break
                j += cycle

        return output
