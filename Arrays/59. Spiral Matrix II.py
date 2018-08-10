# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        temp = [i for i in range(1, (n ** 2) + 1)]
        result = [[None] * n for i in range(n)]

        j = 0
        rowStart, colStart = 0, 0
        rowEnd, colEnd = n, n

        while rowStart < rowEnd and colStart < colEnd:
            for i in range(colStart, colEnd):
                result[rowStart][i] = temp[j]
                j += 1

            rowStart += 1

            for i in range(rowStart, rowEnd):
                result[i][colEnd - 1] = temp[j]
                j += 1

            colEnd -= 1

            if rowStart < rowEnd:
                for i in range(colEnd - 1, colStart - 1, -1):
                    result[rowEnd - 1][i] = temp[j]
                    j += 1

                rowEnd -= 1

            if colStart < colEnd:
                for i in range(rowEnd - 1, rowStart - 1, -1):
                    result[i][colStart] = temp[j]
                    j += 1

                colStart += 1

            if j == len(temp):
                break

        return result