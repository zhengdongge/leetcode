class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True
        s = 1
        while A[s-1] == A[s]:
            s += 1
        if s == len(A) - 1:
            return True
        elif A[s-1] < A[s]:
            i = s + 1
            while i < len(A) - 1:
                if A[i-1] > A[i]:
                    return False
                i += 1
        elif A[0] > A[1]:
            i = s + 1
            while i < len(A) - 1:
                if A[i-1] < A[i]:
                    return False
                i += 1
        return True