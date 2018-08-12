# Given a n-ary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# For example, given a 3-ary tree:
#
#
#
#
#
# We should return its max depth, which is 3.



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        def helper(root):
            if not root:
                return 0
            if not root.children:
                return 1
            maximum = float("-inf")
            for child in root.children:
                maximum = max(maximum, helper(child))
            return maximum + 1

        return helper(root)