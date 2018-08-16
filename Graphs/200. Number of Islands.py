# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
# and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid
# are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3



class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(r, c, R, C, temp):
            if not 0 <= r < R or not 0 <= c < C or grid[r][c] == '0':
                return temp

            temp.extend([r, c])

            grid[r][c] = '0'
            dfs(r - 1, c, R, C, temp)
            dfs(r + 1, c, R, C, temp)
            dfs(r, c - 1, R, C, temp)
            dfs(r, c + 1, R, C, temp)
            return temp

        if not grid or not grid[0]:
            return 0

        R = len(grid)
        C = len(grid[0])

        count = 0
        result = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    count += 1
                    path = dfs(r, c, R, C, [])

        return count