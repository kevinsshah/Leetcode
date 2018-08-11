# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
# corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right



class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        #         C = len(obstacleGrid[0])
        #         R = len(obstacleGrid)

        #         dp = [[0] * (C+1) for _ in range(R+1)]

        #         dp[1][0] = 1

        #         for r in range(1,R+1):
        #             for c in range(1,C+1):
        #                 if not obstacleGrid[r-1][c-1]:
        #                     dp[r][c] += dp[r-1][c] + dp[r][c-1]

        #         return dp[R][C]




        C = len(obstacleGrid[0])
        R = len(obstacleGrid)
        dp = [0] * C
        dp[0] = 1
        for row in obstacleGrid:
            for c, val in enumerate(row):
                if val:
                    dp[c] = 0
                elif c > 0:
                    dp[c] += dp[c - 1]

        return dp[C - 1]