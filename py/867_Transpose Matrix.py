class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        tran_A = [[None]*len(A) for _ in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                tran_A[j][i] = A[i][j]
        return tran_A


t = Solution()
print(t.transpose([[1,2,3],[4,5,6],[7,8,9]]))