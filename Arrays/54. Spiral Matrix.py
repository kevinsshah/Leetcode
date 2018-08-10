# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]



class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix: return []

        rowEnd = len(matrix)
        colEnd = len(matrix[0])
        rowStart = colStart = 0

        result = []

        while rowStart < rowEnd and colStart < colEnd:
            for i in range(colStart, colEnd):
                result.append(matrix[rowStart][i])

            rowStart += 1

            for i in range(rowStart, rowEnd):
                result.append(matrix[i][colEnd - 1])

            colEnd -= 1

            if rowStart < rowEnd:
                for i in range(colEnd - 1, colStart - 1, -1):
                    result.append(matrix[rowEnd - 1][i])

                rowEnd -= 1

            if colStart < colEnd:
                for i in range(rowEnd - 1, rowStart - 1, -1):
                    result.append(matrix[i][colStart])

                colStart += 1

        return result