#problem link-->> https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(n * 2)])
        alt2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(n * 2)])

        count1, count2 = 0, 0
        result = float('inf')

        for i in range(n * 2):
            if s[i] != alt1[i]:
                count1 += 1
            if s[i] != alt2[i]:
                count2 += 1
            if i >= n:
                if s[i - n] != alt1[i - n]:
                    count1 -= 1
                if s[i - n] != alt2[i - n]:
                    count2 -= 1
            if i >= n - 1:
                result = min(result, count1, count2)

        return result
        
