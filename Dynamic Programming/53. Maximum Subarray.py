# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
# largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
# which is more subtle.



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = float("-inf")
        addition = 0

        for i in range(0, len(nums)):
            addition += nums[i]
            addition = max(addition, nums[i])
            ans = max(ans, addition)

        return ans