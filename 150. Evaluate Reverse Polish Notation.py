#problem link-->> https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '*' or i == '+' or i =='/' or i == '-':
                right , left = stack.pop() , stack.pop()
                if i == '*':
                    print(left*right)
                    stack.append(left*right)
                elif i == '+':
                    print(left+right)
                    stack.append(left+right)
                elif i == '-':
                    print(left-right)
                    stack.append(left-right)
                else:
                    if (left/right) < 0:
                        stack.append(math.ceil(left/right))
                    else:
                        stack.append(math.floor(left/right))
            else:
                stack.append(int(i))
        return stack[0]

        
