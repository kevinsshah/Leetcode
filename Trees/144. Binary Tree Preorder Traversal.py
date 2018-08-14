# Given a binary tree, return the preorder traversal of its nodes' values.
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
# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?
#



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        #         result = []
        #         def preorder(root):
        #             if not root:
        #                 return
        #             result.append(root.val)
        #             preorder(root.left)
        #             preorder(root.right)

        #         preorder(root)
        #         return result




        curr = root
        stack = []
        result = []

        while curr or stack:
            if curr:
                stack.append(curr)
                result.append(curr.val)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right

        return result




        #         if not root:
        #             return []

        #         queue = [root]
        #         result = []

        #         while queue:
        #             curr = queue.pop()
        #             result.append(curr.val)
        #             if curr.right:
        #                 queue.append(curr.right)

        #             if curr.left:
        #                 queue.append(curr.left)

        #         return result