# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #         ans = []

        #         def helper(nums,temp,start):
        #             ans.append(list(temp))
        #             for i in range(start,len(nums)):
        #                 temp.append(nums[i])
        #                 helper(nums,temp,i+1)
        #                 temp.pop()

        #         helper(nums,[],0)
        #         return ans



        #         def helper(nums,index):
        #             ans = []
        #             if len(nums) == index:
        #                 ans.append([])
        #             else:
        #                 curr = nums[index]
        #                 remSubsets = helper(nums,index+1)
        #                 ans.extend(remSubsets)
        #                 temp = copy.deepcopy(remSubsets)
        #                 for subset in temp:
        #                     subset.append(curr)
        #                 ans.extend(temp)
        #             return ans

        #         return helper(nums,0)



        def getSet(number, nums):
            index = len(nums) - 1
            result = []
            i = number
            while i > 0:
                if i & 1 == 1:
                    result.append(nums[index])
                i >>= 1
                index -= 1
            return result

        ans = []
        size = 1 << len(nums)
        for i in range(size):
            temp = getSet(i, nums)
            ans.append(temp)

        return ans
