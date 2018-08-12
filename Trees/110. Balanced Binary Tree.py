# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.
#



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        #         def getHeight(root):
        #             if not root:
        #                 return 0
        #             else:
        #                 return max(getHeight(root.left), getHeight(root.right)) + 1


        #         def helper(root):
        #             if not root:
        #                 return True

        #             diff = abs(getHeight(root.left) - getHeight(root.right))
        #             if diff > 1:
        #                 return False
        #             else:
        #                 return helper(root.left) and helper(root.right)

        #         return helper(root)




        def getHeight(root):
            if not root:
                return 0

            left = getHeight(root.left)
            if left == float("-inf"):
                return float("-inf")
            right = getHeight(root.right)
            if right == float("-inf"):
                return float("-inf")

            if abs(left - right) > 1:
                return float("-inf")
            else:
                return max(left, right) + 1

        return getHeight(root) != float("-inf")
