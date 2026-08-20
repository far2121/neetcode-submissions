class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = ""
        cycle = 2 * (numRows - 1)

        for row in range(numRows):
            for i in range(row, len(s), cycle):
                res += s[i]

                # Middle rows have a second character in each cycle
                j = i + cycle - 2 * row

                if row != 0 and row != numRows - 1 and j < len(s):
                    res += s[j]

        return res