# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # return bin(int(a,2) + int(b,2))[2:]

        result = []
        carry = 0

        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = "0" * (len(a) - len(b)) + b

        for i in range(len(a) - 1, -1, -1):
            aDigit = int(a[i])
            bDigit = int(b[i])
            result.append(str((carry + aDigit + bDigit) % 2))
            carry = (carry + aDigit + bDigit) // 2

        if carry > 0:
            result.append(str(carry))

        return "".join(result[::-1])