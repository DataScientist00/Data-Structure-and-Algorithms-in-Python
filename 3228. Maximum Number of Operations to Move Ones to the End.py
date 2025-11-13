# problem link-->> https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description


class Solution:
    def maxOperations(self, s: str) -> int:
        count_one = 0
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == '0':
                ans += count_one
                while i < len(s) and s[i] == '0':
                    i += 1

            else:
                count_one += 1
                i += 1

        return ans

