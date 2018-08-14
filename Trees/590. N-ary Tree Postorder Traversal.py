# Given an n-ary tree, return the postorder traversal of its nodes' values.
#
#
# For example, given a 3-ary tree:
#
#
#
#
# Return its postorder traversal as: [5,6,3,2,4,1].
#
#
# Note: Recursive solution is trivial, could you do it iteratively?





"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        #         def helper(root):
        #             if not root:
        #                 return

        #             for child in root.children:
        #                 helper(child)

        #             result.append(root.val)

        #         result = []
        #         helper(root)
        #         return result



        if not root:
            return []

        queue = [root]
        result = collections.deque()

        while queue:
            curr = queue.pop()
            result.appendleft(curr.val)
            for i in range(len(curr.children)):
                queue.append(curr.children[i])

        return list(result)