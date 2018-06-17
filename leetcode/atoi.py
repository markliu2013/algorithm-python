import math


class Solution:
    @staticmethod
    def reverse(x):
        if str(x).startswith('-'):
            result = int('-' + str(x)[1:][::-1])
        else:
            result = int(str(x)[::-1])
        return 0 if result > (2**31 - 1) or result < -(2**31) else result

    @staticmethod
    def reverse2(x):
        x1 = list(str(abs(x)))
        x1.reverse()
        result = int(''.join(x1)) * (-1 if x < 0 else 1)
        return 0 if result > (2 ** 31 - 1) or result < -(2 ** 31) else result

    @staticmethod
    def reverse3(x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x > 0:
            reminder = x % 10
            x = int(x / 10)
            result = result * 10 + reminder
        result = result * sign
        return 0 if result > (2 ** 31 - 1) or result < -(2 ** 31) else result

print(Solution.reverse3(-1234))
