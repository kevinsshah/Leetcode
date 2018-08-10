# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #         table = []

        #         for rowNum in range(numRows):
        #             row = [None] * (rowNum + 1)
        #             row[0],row[-1] = 1,1

        #             for j in range(1,len(row) - 1):
        #                 row[j] = table[rowNum-1][j-1] + table[rowNum-1][j]

        #             table.append(row)

        #         return table


        answer = [[1] * n for n in range(1, numRows + 1)]

        for i in range(2, numRows):
            for j in range(1, i):
                answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j]

        return answer