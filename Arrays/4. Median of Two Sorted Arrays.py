# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
#
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2,nums1)

        low = 0
        high = m

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = ((m + n + 1) // 2) - cut1

            maxleft1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            minright1 = float("inf") if cut1 == m else nums1[cut1]
            maxleft2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            minright2 = float("inf") if cut2 == n else nums2[cut2]

            if maxleft1 <= minright2 and maxleft2 <= minright1:
                if (m+n) % 2 == 0:
                    return (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2
                else:
                    return max(maxleft1, maxleft2)
            elif maxleft1 > minright2:
                high = cut1 - 1
            else:
                low = cut1 + 1