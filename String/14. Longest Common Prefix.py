# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        #         if strs == []:
        #             return ""

        #         prefix = strs[0]
        #         for i in range(1,len(strs)):
        #             while not strs[i].startswith(prefix):
        #                 prefix = prefix[:-1]
        #                 if prefix == "":
        #                     return prefix

        #         return prefix



        #         def commonPrefix(left, right):
        #             result = []
        #             i = 0
        #             minLength = min(len(left), len(right))
        #             while i < minLength:
        #                 if left[i] != right[i]:
        #                     return left[0:i]
        #                 i += 1
        #             return left[0:minLength]

        #         def helper(strs,l,h):
        #             if l==h:
        #                 return strs[l]
        #             mid = (l + h)//2
        #             left = helper(strs,l,mid)
        #             right = helper(strs,mid + 1,h)
        #             return commonPrefix(left,right)

        #         if strs == []:
        #             return ""

        #         return helper(strs,0,len(strs) - 1)


        if strs == []:
            return ""

        lengthList = list(map(len, strs))
        minLength = min(lengthList)
        shortestWord = strs[lengthList.index(minLength)]

        commonPrefix = []

        for i, char in enumerate(shortestWord):
            for string in strs:
                if string[i] != char:
                    return "".join(commonPrefix)
            commonPrefix.append(char)

        return "".join(commonPrefix)