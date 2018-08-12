# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# Example 1:
#
# Input: "3+2*2"
# Output: 7
# Example 2:
#
# Input: " 3/2 "
# Output: 1
# Example 3:
#
# Input: " 3+5 / 2 "
# Output: 5
# Note:
#
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.



class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = '+'
        num = 0
        stack = []

        for i, c in enumerate(s):
            if c.isdigit():
                num = (ord(c) - ord('0')) + (num * 10)
            if i == len(s) - 1 or (not c.isdigit() and c != " "):
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        return sum(stack)