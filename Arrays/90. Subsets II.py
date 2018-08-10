# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def helper(nums, temp, start):
            ans.append(list(temp))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]: continue
                temp.append(nums[i])
                helper(nums, temp, i + 1)
                temp.pop()

        nums = sorted(nums)
        helper(nums, [], 0)

        return ans