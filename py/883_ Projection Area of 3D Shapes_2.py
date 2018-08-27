class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = 0
        f = 0
        r = 0
        for i in range(0, len(grid)):
                f += max(grid[i])
        for j in range(0, len(grid[0])):
            maxt = grid[0][j]
            for i in range(0, len(grid)):
                if grid[i][j] > maxt:
                    maxt = grid[i][j]
                if grid[i][j] != 0:
                    h += 1
            r += maxt

        return (h + f + r)


t = Solution()
print(t.projectionArea([[1,2],[3,4]]))
print(t.projectionArea([[1,1,1],[1,0,1],[1,1,1]]))
print(t.projectionArea([[2,2,2],[2,1,2],[2,2,2]]))






