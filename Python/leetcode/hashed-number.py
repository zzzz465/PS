"""
An integer divisible by the sum of its digits is said to be a Harshad number.
You are given an integer x.
Return the sum of the digits of x if x is a Harshad number, otherwise, return -1
"""

# it only tooks 2 minutes to solve. literally


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digits = [int(c) for c in str(x)]

        if x % sum(digits) == 0:
            return sum(digits)
        else:
            return -1
