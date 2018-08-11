# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:
#
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
#              Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.



class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= len(prices) // 2:
            T_i0 = 0
            T_i1 = float("-inf")

            for price in prices:
                temp = T_i0
                T_i0 = max(T_i0, T_i1 + price)
                T_i1 = max(T_i1, temp - price)

            return T_i0

        T_i0 = [0] * (k + 1)
        T_i1 = [float("-inf")] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                T_i0[i] = max(T_i0[i], T_i1[i] + price)
                T_i1[i] = max(T_i1[i], T_i0[i - 1] - price)
        return T_i0[k]