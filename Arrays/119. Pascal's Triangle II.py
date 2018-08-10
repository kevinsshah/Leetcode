# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 3
# Output: [1,3,3,1]


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        prev = []
        for rowNum in range(rowIndex + 1):
            curr = [1] * (len(prev) + 1)
            for j in range(1, len(curr) - 1):
                curr[j] = prev[j - 1] + prev[j]
            prev = curr

        return curr