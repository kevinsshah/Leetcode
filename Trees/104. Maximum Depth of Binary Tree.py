# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        #         def helper(root):
        #             if root == None:
        #                 return 0
        #             if root.left == None and root.right == None:
        #                 return 1

        #             left = helper(root.left)
        #             right = helper(root.right)
        #             return (max(left,right) + 1)

        #         return helper(root)


        ans, q = 0, []
        if not root: return ans
        q.append(root)
        while q:
            tempq = []
            for elem in q:
                if elem.left: tempq.append(elem.left)
                if elem.right: tempq.append(elem.right)
            q = tempq
            ans += 1

        return ans