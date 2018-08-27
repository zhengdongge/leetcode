class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left, right+1):
            sd = True
            str_num = str(num)
            for i in range(0, len(str_num)):
                j = int(str_num[i])
                if j == 0:
                    sd = False
                    break
                elif num % j != 0:
                    sd = False
                    break
            if sd:
                result.append(num)

        return result


test = Solution()
print(test.selfDividingNumbers(9,22))