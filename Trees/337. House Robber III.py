# The thief has found himself a new place for his thievery again. There is only one entrance to this area,
# called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#
# Input: [3,4,5,1,3,null,1]
#
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
#
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.




class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        #         table = {}

        #         def helper(root):
        #             if not root:
        #                 return 0

        #             if root in table:
        #                 return table[root]

        #             val = root.val
        #             if root.left:
        #                 val += helper(root.left.left) + helper(root.left.right)
        #             if root.right:
        #                 val += helper(root.right.left) + helper(root.right.right)

        #             val = max(val,helper(root.left) + helper(root.right))
        #             table[root] = val
        #             return val

        #         return helper(root)




        def helper(root):
            if not root:
                return [0, 0]
            res = [0, 0]

            left = helper(root.left)
            right = helper(root.right)

            res[0] = root.val + left[1] + right[1]
            res[1] = max(left) + max(right)

            return res

        res = helper(root)
        return max(res)