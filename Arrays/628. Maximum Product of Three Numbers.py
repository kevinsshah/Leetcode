# Given an integer array, find three numbers whose product is maximum and output the maximum product.
#
# Example 1:
# Input: [1,2,3]
# Output: 6
# Example 2:
# Input: [1,2,3,4]
# Output: 24
# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = float("-inf")
        second = float("-inf")
        third = float("-inf")
        last = float("inf")
        secondLast = float("inf")

        for num in nums:
            if num >= first:
                third = second
                second = first
                first = num
            elif num >= second:
                third = second
                second = num
            elif num >= third:
                third = num

            if num <= last:
                secondLast = last
                last = num
            elif num <= secondLast:
                secondLast = num

        return max(first * second * third, first * last * secondLast)