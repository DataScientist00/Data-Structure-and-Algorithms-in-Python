# problem link-->> https://leetcode.com/problems/count-number-of-trapezoids-i/description/


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        lookup = {}
        mod = int(10 ** 9 + 7)
        for x,y in points:
            if y not in lookup:
                lookup[y] = 1
            else:
                lookup[y] += 1

        ans = 0
        total = 0
        prev = 0
        permut = 0
        for val in lookup.values():
            permut = val * (val-1) // 2
            ans += permut * total
            total += permut
        return ans % mod
