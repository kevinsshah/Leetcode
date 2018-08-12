# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #         stack = []

        #         for i,char in enumerate(s):
        #             if char == ")":
        #                 if not stack: return False
        #                 top = stack.pop()
        #                 if top != "(":
        #                     return False
        #             elif char == "]":
        #                 if not stack: return False
        #                 top = stack.pop()
        #                 if top != "[":
        #                     return False
        #             elif char == "}":
        #                 if not stack: return False
        #                 top = stack.pop()
        #                 if top != "{":
        #                     return False
        #             else:
        #                 stack.append(char)

        #         return len(stack) == 0

        stack = []
        table = {"}": "{", ")": "(", "]": "["}
        for char in s:
            if char in table.values():
                stack.append(char)
            elif char in table.keys():
                if stack == [] or table[char] != stack.pop():
                    return False
        return stack == []
