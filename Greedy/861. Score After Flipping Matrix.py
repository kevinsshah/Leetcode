# We have a two dimensional matrix A where each value is 0 or 1.
#
# A move consists of choosing any row or column, and toggling each value in that row or column:
# changing all 0s to 1s, and all 1s to 0s.
#
# After making any number of moves, every row of this matrix is interpreted as a binary number,
# and the score of the matrix is the sum of these numbers.
#
# Return the highest possible score.
#
#
#
# Example 1:
#
# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
#
# Note:
#
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] is 0 or 1.




class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        #         R = len(A)
        #         C = len(A[0])

        #         count = [0] * C

        #         def flipRow(A,row):
        #             for c in range(C):
        #                 A[row][c] ^= 1

        #         def flipCol(A,col):
        #             for r in range(R):
        #                 A[r][col] ^= 1

        #         for r in range(R):
        #             if A[r][0] == 0:
        #                 flipRow(A,r)
        #             for c in range(C):
        #                 if A[r][c] == 1:
        #                     count[c] += 1

        #         for c in range(C):
        #             if count[c] <= R//2:
        #                 flipCol(A,c)

        #         result = 0

        #         for r in range(R):
        #             sum = 0
        #             for c in range(C-1, -1, -1):
        #                 if A[r][c] == 1:
        #                     sum += 2 ** (C-c-1)
        #             result += sum

        #         return result






        R = len(A)
        C = len(A[0])

        result = (1 << C - 1) * R

        for c in range(1, C):
            same = 0
            for r in range(R):
                if A[r][c] == A[r][0]:
                    same += 1
            result += max(same, R - same) * (2 ** (C - c - 1))
        return result