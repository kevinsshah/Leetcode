# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.



class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isPali(low, high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        for i in range(0, len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return isPali(i, j - 1) or isPali(i + 1, j)

        return True