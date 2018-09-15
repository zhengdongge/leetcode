class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            pair = target - nums[i]
            if d.__contains__(pair) and d[pair] != i:
                return (i, d[pair])


t = Solution()
print(t.twoSum([3,2,4], 6))