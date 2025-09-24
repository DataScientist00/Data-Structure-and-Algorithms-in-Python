# problem link-->> https://leetcode.com/problems/fraction-to-recurring-decimal/description


class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n == 0:
            return '0' 

        fraction = []
        if (n < 0) != (d < 0):
            fraction.append('-')

        n = abs(n)
        d = abs(d)
        fraction.append(str(n//d))
        remainder = n%d
        if remainder == 0:
            return ''.join(fraction)

        fraction.append('.')
        dict_map = {}
        while remainder != 0:
            if remainder in dict_map:
                fraction.insert(dict_map[remainder] , '(')
                fraction.append(')')
                break
            dict_map[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder//d))
            remainder %= d
        return ''.join(fraction)
        
