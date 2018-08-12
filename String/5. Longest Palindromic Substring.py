# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


class Solution:
    def __init__(self):
        self.low = 0
        self.length = float("-inf")

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        #         if len(s) < 2:
        #             return s

        #         def extendPalindrome(l,r):
        #             while l >= 0 and r < len(s) and s[l] == s[r]:
        #                 l -= 1
        #                 r += 1
        #             if self.length < r - l - 1:
        #                 self.low = l + 1
        #                 self.length = r - l -1


        #         for i in range(len(s)):
        #             extendPalindrome(i, i)
        #             extendPalindrome(i, i+1)

        #         return s[self.low: self.low + self.length]



        maxLen = 1
        start = 0
        for i in range(len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1

        return s[start:start + maxLen]