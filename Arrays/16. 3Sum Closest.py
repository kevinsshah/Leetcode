# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest
# to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        ans = float("inf")
        nums = sorted(nums)
        for i in range(0, len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                temp = nums[i] + nums[low] + nums[high]
                if abs(temp - target) < abs(ans - target):
                    ans = temp

                if temp == target:
                    return temp
                elif temp > target:
                    high -= 1
                else:
                    low += 1

        return ans