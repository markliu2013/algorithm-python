class Solution:
    @staticmethod
    def reverse(x):
        if str(x).startswith('-'):
            result = int('-' + str(x)[1:][::-1])
        else:
            result = int(str(x)[::-1])
        return 0 if result > (2**31 - 1) or result < -(2**31) else result

print(Solution.reverse(-2147483648))
