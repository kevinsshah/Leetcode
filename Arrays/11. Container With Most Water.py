# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
#  n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
#  Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # ans = float("-inf")
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         val = (j - i) * min(height[j],height[i])
        #         ans = max(ans, val)
        # return ans


        i = 0
        j = len(height) - 1
        ans = 0

        while i < j:
            if height[i] < height[j]:
                val = (j - i) * height[i]
                i += 1
            else:
                val = (j - i) * height[j]
                j -= 1
            ans = max(ans, val)
        return ans