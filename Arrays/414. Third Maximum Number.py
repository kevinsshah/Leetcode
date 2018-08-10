# Given a non-empty array of integers, return the third maximum number in this array.
# If it does not exist, return the maximum number. The time complexity must be in O(n).
#
# Example 1:
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.



class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #         nums = sorted(nums,reverse = True)

        #         count = 1
        #         for i in range(1,len(nums)):
        #             if nums[i] != nums[i-1]:
        #                 count+=1
        #             if count == 3:
        #                 break

        #         return nums[i] if count==3 else nums[0]


        first = float("-inf")
        second = float("-inf")
        third = float("-inf")

        for i in range(0, len(nums)):
            if nums[i] == first or nums[i] == second or nums[i] == third:
                continue
            if nums[i] > first:
                third = second
                second = first
                first = nums[i]
            elif nums[i] > second:
                third = second
                second = nums[i]
            elif nums[i] > third:
                third = nums[i]

        return third if third != float("-inf") else first