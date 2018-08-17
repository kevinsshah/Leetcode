# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        #         def helper(preStart, inStart, inEnd):
        #             if preStart >= len(preorder) or inStart > inEnd:
        #                 return None
        #             node = TreeNode(preorder[preStart])

        #             for i in range(inStart, inEnd + 1):
        #                 if inorder[i] == node.val:
        #                     break

        #             node.left = helper(preStart + 1, inStart, i - 1)
        #             node.right = helper(preStart + i - inStart + 1, i + 1, inEnd)
        #             return node


        #         return helper(0, 0, len(inorder) - 1)


        def helper(preStart, inStart, inEnd):
            if preStart >= len(preorder) or inStart > inEnd:
                return None
            node = TreeNode(preorder[preStart])
            i = index[node.val]
            node.left = helper(preStart + 1, inStart, i - 1)
            node.right = helper(preStart + i - inStart + 1, i + 1, inEnd)
            return node

        index = {c: i for i, c in enumerate(inorder)}
        return helper(0, 0, len(inorder) - 1)
