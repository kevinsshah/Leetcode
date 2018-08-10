# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that
# a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        if len(nums) < 4:
            return ans

        nums = sorted(nums)
        for i in range(len(nums) - 3):

            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                for j in range(i + 1, len(nums) - 2):

                    if j == i + 1 or (j > i + 1 and nums[j] != nums[j - 1]):
                        low = j + 1
                        high = len(nums) - 1
                        while low < high:
                            sum = nums[i] + nums[j] + nums[low] + nums[high]
                            if sum == target:
                                ans.append([nums[i], nums[j], nums[low], nums[high]])
                                while low < high and nums[low] == nums[low + 1]:
                                    low += 1
                                while low < high and nums[high] == nums[high - 1]:
                                    high -= 1
                                low += 1
                                high -= 1
                            elif sum < target:
                                low += 1
                            else:
                                high -= 1

        return ans