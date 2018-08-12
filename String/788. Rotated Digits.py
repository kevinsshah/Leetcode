# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is
# different from X.  Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5
# rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
#
# N  will be in range [1, 10000].


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        # def isDigit(digit):
        #     if digit == "0" or digit == "1" or digit == "8":
        #         return digit
        #     elif digit == "2":
        #         return "5"
        #     elif digit == "5":
        #         return "2"
        #     elif digit == "6":
        #         return "9"
        #     elif digit == "9":
        #         return "6"
        #     else: return -1

        def isGoodNum(num):
            validFound = False
            while num > 0:
                if num % 10 == 2: validFound = True
                if num % 10 == 5: validFound = True
                if num % 10 == 6: validFound = True
                if num % 10 == 9: validFound = True
                if num % 10 == 3: return False
                if num % 10 == 4: return False
                if num % 10 == 7: return False
                num //= 10

            return validFound
            # s = str(num)
            # result = ""
            # for digit in s:
            #     rotated = isDigit(digit)
            #     if rotated == -1:
            #         return rotated
            #     else:
            #         result += rotated
            # return int(result)

        ans = 0
        for i in range(1, N + 1):
            if isGoodNum(i):
                ans += 1

        return ans