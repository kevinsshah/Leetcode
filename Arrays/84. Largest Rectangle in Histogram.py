# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#
#
# Example:
#
# Input: [2,1,5,6,2,3]
# Output: 10




class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #         ans = 0

        #         for i in range(len(heights)):
        #             mini = float("inf")
        #             for j in range(i,len(heights)):
        #                 mini = min(mini,heights[j])
        #                 ans = max(ans, mini * (j-i+1))

        #         return ans





        #         def helper(low,high):
        #             if low > high:
        #                 return 0
        #             mini = low
        #             for i in range(low,high + 1):
        #                 if heights[i] < heights[mini]:
        #                     mini = i

        #             return max(heights[mini] * (high - low + 1), helper(low,mini-1), helper(mini+1,high))


        #         return helper(0,len(heights) - 1)




        #         stack = []
        #         i = 0
        #         ans = 0
        #         while i < len(heights):
        #             if not stack or heights[stack[-1]] <= heights[i]:
        #                 stack.append(i)
        #                 i += 1
        #             else:
        #                 top = stack.pop()
        #                 area = heights[top] * (i - stack[-1] - 1 if stack else i)
        #                 ans = max(ans,area)

        #         while stack:
        #             top = stack.pop()
        #             area = heights[top] * (i - stack[-1] - 1 if stack else i)
        #             ans = max(ans,area)
        #         return ans



        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans