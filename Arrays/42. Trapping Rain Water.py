# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #         ans = 0
        #         for i in range(1,len(height) - 1):
        #             left_max = float("-inf")
        #             right_max = float("-inf")

        #             for j in range(i, -1, -1):
        #                 left_max = max(left_max,height[j])
        #             for j in range(i,len(height)):
        #                 right_max = max(right_max,height[j])

        #             ans += min(left_max, right_max) - height[i]

        #         return ans





        #         if not height:
        #             return 0

        #         left_max = [0] * len(height)
        #         right_max = [0] * len(height)
        #         ans = 0

        #         left_max[0] = height[0]

        #         for j in range(1,len(height)):
        #             left_max[j] = max(left_max[j-1],height[j])

        #         right_max[-1] = height[-1]

        #         for j in range(len(height) - 2, -1, -1):
        #             right_max[j] = max(right_max[j+1],height[j])

        #         for i in range(1,len(height) - 1):
        #             ans += min(left_max[i],right_max[i]) - height[i]

        #         return ans




        left = 0
        right = len(height) - 1
        left_max = float("-inf")
        right_max = float("-inf")
        ans = 0

        # while left < right:
        #     left_max = max(left_max,height[left])
        #     right_max = max(right_max,height[right])
        #     if left_max < right_max:
        #         ans += left_max - height[left]
        #         left += 1
        #     else:
        #         ans += right_max - height[right]
        #         right -= 1
        # return ans

        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    ans += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    ans += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1

        return ans