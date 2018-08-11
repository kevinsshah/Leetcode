# Given a positive integer n, break it into the sum of at least two positive integers and maximize the
# product of those integers. Return the maximum product you can get.
#
# Example 1:
#
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:
#
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# Note: You may assume that n is not less than 2 and not larger than 58.
#


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [float("-inf")] * (n + 1)
        # dp[1] = 0
        dp[2] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))

        return dp[n]





        #         if n==2 or n==3:
        #             return n-1

        #         res = 1
        #         while n > 4:
        #             n -= 3
        #             res *= 3

        #         return res * n