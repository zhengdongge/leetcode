class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        linecharcount = 0
        for char in S:
            if widths[ord(char) - ord('a')] + linecharcount <= 100:
                linecharcount += widths[ord(char) - ord('a')]
            else:
                lines +=1
                linecharcount = widths[ord(char) - ord('a')]
        return [lines, linecharcount]

