# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        #         def helper(A = []):
        #             if len(A) == 2*n:
        #                 if isValid(A):
        #                     ans.append("".join(A))
        #             else:
        #                 A.append("(")
        #                 helper(A)
        #                 A.pop()
        #                 A.append(")")
        #                 helper(A)
        #                 A.pop()

        #         def isValid(A):
        #             bal = 0
        #             for c in A:
        #                 if c == "(":
        #                     bal+=1
        #                 else:
        #                     bal -= 1
        #                 if bal < 0:
        #                     return False
        #             return bal == 0


        #         ans = []
        #         helper()

        #         return ans





        #         def backtrack(S = '', left = 0, right = 0):
        #             if len(S) == 2*n:
        #                 ans.append(S)
        #                 return
        #             if left < n:
        #                 backtrack(S+"(", left + 1, right)
        #             if right < left:
        #                 backtrack(S+")", left, right + 1)

        #         ans = []
        #         backtrack()
        #         return ans




        ans = []

        def helper(left, right, string, ans):
            if right < left:
                return
            if not left and not right:
                ans.append(string)
                return
            if left:
                helper(left - 1, right, string + "(", ans)
            if right:
                helper(left, right - 1, string + ")", ans)

        helper(n, n, "", ans)
        return ans