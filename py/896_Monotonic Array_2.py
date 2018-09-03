def isMonotonic(self, A):
    return not {cmp(i, j) for i, j in zip(A, A[1:])} >= {1, -1}