# problem link-->> https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/


class Solution:
    def numOfWays(self, n: int) -> int:
        
        M = 10**9 + 7
        states = ["RGB", "RBG", "GRB", "GBR", "BRG", "BGR","RGR", "RBR", "GRG", "GBG", "BRB", "BGB"]
        t = [[-1] * 12 for _ in range(n)]

        def solve(rows_left, prev):
            if rows_left == 0:
                return 1

            if t[rows_left][prev] != -1:
                return t[rows_left][prev]

            result = 0
            last = states[prev]

            for curr in range(12):
                if curr == prev:
                    continue

                currPat = states[curr]
                conflict = False

                for col in range(3):
                    if currPat[col] == last[col]:
                        conflict = True
                        break

                if not conflict:
                    result = (result + solve(rows_left - 1, curr)) % M

            t[rows_left][prev] = result
            return result

        result = 0
        for i in range(12):
            result = (result + solve(n - 1, i)) % M

        return result
