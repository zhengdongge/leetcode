import copy
class Solution:
    def flipAndInvertImage(a):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        new_a = copy.deepcopy(a)
        for i in range(0, len(a)):
            for j in range(0, len(a[i])):
                new_a[i][j] = 1 - a[i][len(a[i])-j-1]
        return new_a


    print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))