class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for jewel in J:
            for char in S:
                if char == jewel:
                    count += 1
        return count
