# problem link-->> https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return True
        stack = []
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == ')' and not stack:
                ans += 1
            elif s[i] == ')' and stack:
                stack.pop()
        return ans + len(stack)

        
        
