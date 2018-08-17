# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        #         def helper(postEnd, inStart, inEnd):
        #             if postEnd < 0 or inStart > inEnd:
        #                 return None
        #             node = TreeNode(postorder[postEnd])
        #             for i in range(inStart, inEnd + 1):
        #                 if inorder[i] == node.val:
        #                     break

        #             node.right = helper(postEnd - 1, i + 1, inEnd)
        #             node.left = helper(postEnd - (inEnd - i + 1), inStart, i - 1)
        #             return node

        #         return helper(len(postorder) - 1, 0, len(inorder) - 1)



        def helper(postEnd, inStart, inEnd):
            if postEnd < 0 or inStart > inEnd:
                return None
            node = TreeNode(postorder[postEnd])
            i = index[node.val]
            node.right = helper(postEnd - 1, i + 1, inEnd)
            node.left = helper(postEnd - (inEnd - i + 1), inStart, i - 1)
            return node

        index = {c: i for i, c in enumerate(inorder)}
        return helper(len(postorder) - 1, 0, len(inorder) - 1)
