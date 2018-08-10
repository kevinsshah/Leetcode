# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
# Example 1:
#
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:
#
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?



class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowHasZero = False
        colHasZero = False

        for i in range(0, len(matrix[0])):
            if matrix[0][i] == 0:
                rowHasZero = True
                break

        for j in range(0, len(matrix)):
            if matrix[j][0] == 0:
                colHasZero = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if (matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                self.nullifyRows(matrix, i)

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                self.nullifyCols(matrix, j)

        if rowHasZero:
            self.nullifyRows(matrix, 0)

        if colHasZero:
            self.nullifyCols(matrix, 0)

    def nullifyRows(self, matrix, row):
        for i in range(0, len(matrix[0])):
            matrix[row][i] = 0

    def nullifyCols(self, matrix, col):
        for j in range(0, len(matrix)):
            matrix[j][col] = 0
