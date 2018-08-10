# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        for i in range(1, len(nums)):
            a = a ^ nums[i]

        b = 0
        for i in range(len(nums) + 1):
            b = b ^ i

        return a ^ b




        #         missing = len(nums)
        #         for i,num in enumerate(nums):
        #             missing ^= i ^ num

        #         return missing




        #         expected = sum(nums)

        #         actual = (len(nums)* (len(nums) + 1))//2

        #         return actual - expected  