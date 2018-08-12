# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ans = collections.defaultdict(list)
        for s in strs:
            ans["".join(sorted(s))].append(s)

        return list(ans.values())



        #         ans = collections.defaultdict(list)
        #         for string in strs:
        #             count = [0] * 26
        #             for c in string:
        #                 count[ord(c) - ord('a')] +=1

        #             ans[tuple(count)].append(string)

        #         return list(ans.values())