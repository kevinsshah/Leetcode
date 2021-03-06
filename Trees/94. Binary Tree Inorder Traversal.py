# Given a binary tree, return the inorder traversal of its nodes' values.
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
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #         result = []

        #         def helper(root,result):
        #             if root == None:
        #                 return
        #             helper(root.left, result)
        #             result.append(root.val)
        #             helper(root.right, result)

        #         helper(root,result)

        #         return result




        curr = root
        stack = []
        result = []

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right

        return result