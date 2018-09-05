class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True
        s = 1
        while A[s-1] == A[s] and s < len(A) - 1:
            s += 1
        if s == len(A) - 1:
            return True
        elif A[s-1] < A[s]:
            i = s
            while i <= len(A) - 1:
                if A[i-1] > A[i]:
                    return False
                i += 1
        elif A[s-1] > A[s]:
            i = s
            while i <= len(A) - 1:
                if A[i-1] < A[i]:
                    return False
                i += 1
        return True


t = Solution()
print(t.isMonotonic([1,3,2]))