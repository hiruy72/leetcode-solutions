class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Base case: if numRows == 1 or string is too short
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows  # list of strings for each row
        index, step = 0, 1  # track current row and direction

        for char in s:
            rows[index] += char
            # Change direction when reaching top or bottom
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        # Join all rows together
        return ''.join(rows)

        