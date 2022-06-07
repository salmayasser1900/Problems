class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle.upper()
        number = 0

        for ch in columnTitle:
            number = number * 26
            number += ord(ch) - ord('A') + 1

        return number
        