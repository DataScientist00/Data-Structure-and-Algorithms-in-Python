#problem link-->> https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[' :
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                elif stack[-1] =='[' and i == ']':
                    stack.pop()
                else:
                    return False
        return stack == [] 

        
