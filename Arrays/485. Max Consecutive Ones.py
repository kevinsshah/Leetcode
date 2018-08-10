# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #         count = 0
        #         ans = float("-inf")

        #         for num in nums:
        #             if num != 1:
        #                 ans = max(ans,count)
        #                 count = 0
        #             else:
        #                 count += 1

        #         return max(ans,count)



        ans = float("-inf")
        low = 0
        high = 0
        zero = 0
        k = 0
        while high < len(nums):
            if nums[high] == 0:
                zero += 1
            while zero > k:
                if nums[low] == 0:
                    zero -= 1
                low += 1
            ans = max(ans, high - low + 1)

            high += 1

        return ans