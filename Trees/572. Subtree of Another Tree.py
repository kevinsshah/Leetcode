# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values
# with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def preorder(root):
            if not root:
                return ['X']
            result = [str(root.val)]
            left = preorder(root.left)
            right = preorder(root.right)
            result = result + left + right
            return result

        a = " ".join(preorder(s))
        b = " ".join(preorder(t))
        a = " " + a
        b = " " + b

        if a.find(b) == -1:
            return False
        else:
            return True

# def match(s,t):
#             if not s and not t:
#                 return True
#             elif not s or not t:
#                 return False
#             elif s.val != t.val:
#                 return False
#             else:
#                 return match(s.left,t.left) and match(s.right,t.right)


#         def subtree(s,t):
#             if not s:
#                 return False
#             if s.val == t.val and match(s,t):
#                 return True
#             return subtree(s.left,t) or subtree(s.right,t)

#         if not t:
#             return True
#         return subtree(s,t)
