#problem link--->>> https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def rec(openp, closep):
            if openp == closep == n:
                res.append("".join(stack))
                return
            
            if openp < n:
                stack.append("(")
                rec(openp+1 , closep)
                stack.pop()
            
            if closep < openp:
                stack.append(")")
                rec(openp , closep+1)
                stack.pop()
        rec(0,0)
        return res
        
