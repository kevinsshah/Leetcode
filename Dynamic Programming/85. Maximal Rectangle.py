# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# Example:
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6


class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        R = len(matrix)
        C = len(matrix[0])

        heights = [0] * (C + 1)
        ans = 0

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            stack = [-1]
            for c in range(C + 1):
                while heights[stack[-1]] > heights[c]:
                    h = heights[stack.pop()]
                    w = c - stack[-1] - 1
                    ans = max(ans, w * h)
                stack.append(c)

        return ans






        #         if not matrix or not matrix[0]:
        #             return 0

        #         R = len(matrix)
        #         C = len(matrix[0])

        #         heights = [0] * (C)
        #         ans = 0

        #         for r in range(R):
        #             for c in range(C):
        #                 if matrix[r][c] == '1':
        #                     heights[c] += 1
        #                 else:
        #                     heights[c] = 0

        #             stack = []
        #             c = 0

        #             while c < C:
        #                 if not stack or heights[c] >= heights[stack[-1]]:
        #                     stack.append(c)
        #                     c += 1
        #                 else:
        #                     top = stack.pop()
        #                     area = heights[top] * (c - stack[-1] - 1 if stack else c)
        #                     ans = max(ans,area)

        #             while stack:
        #                 top = stack.pop()
        #                 area = heights[top] * (c - stack[-1] - 1 if stack else c)
        #                 ans = max(ans,area)

        #         return ans