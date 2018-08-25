class Solution:
    def flipAndInvertImage(A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        new_a = []
        for i in range[0, len(A)-1]:
            for j in range[0, len(A[i])-1]:
                new_a[i, j] = 1-A[i, len(A[i])-j-1]
        return new_a


    print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))