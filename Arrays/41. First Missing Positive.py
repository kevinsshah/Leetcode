# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #         table = set()
        #         for num in nums:
        #             if num > 0:
        #                 table.add(num)

        #         i = 1
        #         while True:
        #             if i not in table:
        #                 return i
        #             i += 1


        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = len(nums) + 1

        for i, num in enumerate(nums):
            num = abs(num)
            if num <= len(nums):
                nums[num - 1] = 0 - abs(nums[num - 1])

        for i, num in enumerate(nums):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1