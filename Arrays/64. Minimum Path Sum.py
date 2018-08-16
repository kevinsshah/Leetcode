# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the
# sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.



class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R = len(grid)
        C = len(grid[0])

        dp = [[0] * C for _ in range(R)]

        dp[0][0] = grid[0][0]

        for i in range(1, C):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, R):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for r in range(1, R):
            for c in range(1, C):
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

        return dp[R - 1][C - 1]