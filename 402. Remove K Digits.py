#problem link-->> https://leetcode.com/problems/remove-k-digits/description/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            if i  == '0' and not stack:
                    continue
            else:
                stack.append(i)
        stack = stack[:len(stack)-k]
        res= ''.join(stack)
        return res if stack else '0'
        
