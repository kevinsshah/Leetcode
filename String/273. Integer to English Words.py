# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
# Input: 123
# Output: "One Hundred Twenty Three"
# Example 2:
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        before10 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        before20 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                    "Nineteen"]
        before100 = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def helper(num):
            result = ""

            if num < 10:
                result += before10[num]
            elif num < 20:
                result += before20[num - 10]
            elif num < 100:
                result += before100[num // 10] + " " + helper(num % 10)
            elif num < 1000:
                result += helper(num // 100) + " Hundred " + helper(num % 100)
            elif num < 1000000:
                result += helper(num // 1000) + " Thousand " + helper(num % 1000)
            elif num < 1000000000:
                result += helper(num // 1000000) + " Million " + helper(num % 1000000)
            else:
                result += helper(num // 1000000000) + " Billion " + helper(num % 1000000000)

            return result.strip()

        if num == 0:
            return "Zero"
        else:
            return helper(num)