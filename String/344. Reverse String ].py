# Write a function that takes a string as input and returns the string reversed.
#
# Example 1:
#
# Input: "hello"
# Output: "olleh"
# Example 2:
#
# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        j = len(s) - 1

        result = []

        for i in range(len(s) - 1, -1, -1):
            result.append(s[i])

        return ''.join(result)