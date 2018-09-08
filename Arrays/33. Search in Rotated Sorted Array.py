# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1



class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #         if len(nums)==0:
        #             return -1

        #         def searchInner(nums,target,low,high):
        #             if low>high:
        #                 return -1
        #             mid = (low + high)//2
        #             if nums[mid] == target:
        #                 return mid
        #             elif nums[mid] < target:
        #                 return searchInner(nums,target,mid+1,high)
        #             else:
        #                 return searchInner(nums,target,low,mid-1)


        #         low = 0
        #         high = len(nums)-1
        #         while(low<high):
        #             mid = (low+high)//2
        #             if nums[mid] > nums[high]:
        #                 low = mid+1
        #             else:
        #                 high = mid


        #         actualLow = low

        #         if target>=nums[0]:
        #             low = 0
        #             high = len(nums) - 1 if actualLow==0 else actualLow - 1
        #         else:
        #             low = actualLow
        #             high = len(nums) - 1

        #         return searchInner(nums,target,low,high)

        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[low]:
                if (nums[low] <= target < nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if (nums[mid] < target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
