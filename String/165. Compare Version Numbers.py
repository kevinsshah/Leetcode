# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level
# revision of the second first-level revision.
#
# Example 1:
#
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# Example 2:
#
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
# Example 3:
#
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        list1 = version1.split(".")
        list2 = version2.split(".")

        len1 = len(list1)
        len2 = len(list2)

        for i in range(max(len1, len2)):
            v1 = int(list1[i]) if i < len1 else 0
            v2 = int(list2[i]) if i < len2 else 0
            compare = (v1 > v2) - (v2 > v1)
            print(v1, v2, compare)
            if compare != 0:
                return compare

        return 0