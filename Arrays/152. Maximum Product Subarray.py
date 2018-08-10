# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        imax = nums[0]
        imin = nums[0]

        ans = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if num < 0:
                temp = imax
                imax = imin
                imin = temp

            imax = max(imax * num, num)
            imin = min(imin * num, num)

            ans = max(ans, imax)

        return ans if ans != float("-inf") else 0
