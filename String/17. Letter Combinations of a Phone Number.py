# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the
# number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does
# not map to any letters.
#
#
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#


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
