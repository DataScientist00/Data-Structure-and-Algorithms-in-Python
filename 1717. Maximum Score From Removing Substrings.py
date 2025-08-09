# problem link-->> https://leetcode.com/problems/maximum-score-from-removing-substrings/description/

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def max_score(st , sc):
            res = 0
            nonlocal s
            stack = []
            for c in s:
                if stack and stack[-1] == st[0] and c == st[1]:
                    stack.pop()
                    res += sc
                else:
                    stack.append(c)
            s = ''.join(stack)
            return res

        score = 0
        pair = 'ab' if x > y else 'ba'
        score += max_score(pair , max(x , y))
        score += max_score(pair[::-1] , min(x , y))
        return score
        

            
        
