# problem link-->> https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        temp = []
        stack = []
        for c in s:
            if c == ")":
                temp = []
                while stack[-1] != '(':
                    t = stack.pop()
                    temp.append(t)
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(c)
        return "".join(stack)

                
        
