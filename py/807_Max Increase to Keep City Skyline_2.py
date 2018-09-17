class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        collen = len(grid)
        rowlen = len(grid[0])
        result = 0
        #incgrid =[[0 for col in range(collen)] for row in range(rowlen)]
        rowmax = []
        for j in range(rowlen):
            rowmax.append(grid[0][j])
            for i in range(collen):
                if grid[i][j] > rowmax[j]:
                    rowmax[j] = grid[i][j]
        for i in range(collen):
            colmax = max(grid[i])
            for j in range(rowlen):
                result += min(colmax, rowmax[j]) - grid[i][j]
        return result


t = Solution()
print(t.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))

