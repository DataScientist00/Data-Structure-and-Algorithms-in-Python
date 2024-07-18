#problem link-->> https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/


class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxx = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                maxx = max(count , maxx)
            if s[i] == ')':
                count -= 1
        return maxx
