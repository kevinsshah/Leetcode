# Given a binary tree, return the postorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        #         def postorder(root):
        #             if not root:
        #                 return

        #             postorder(root.left)
        #             postorder(root.right)
        #             result.append(root.val)

        #         result = []

        #         postorder(root)

        #         return result




        curr = root
        stack = []
        result = collections.deque()

        while curr or stack:
            if curr:
                stack.append(curr)
                result.appendleft(curr.val)
                curr = curr.right
            else:
                curr = stack.pop()
                curr = curr.left
        return list(result)




        #         if not root:
        #             return []

        #         queue = [root]
        #         result = collections.deque()

        #         while queue:
        #             curr = queue.pop()
        #             result.appendleft(curr.val)
        #             if curr.left:
        #                 queue.append(curr.left)
        #             if curr.right:
        #                 queue.append(curr.right)

        #         return list(result)