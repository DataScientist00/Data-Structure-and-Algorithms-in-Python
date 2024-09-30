#problem link-->> https://leetcode.com/problems/maximum-number-of-balloons/description/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counttext = Counter(text)
        count = Counter('balloon')
        a = len(text)
        for i in 'balloon':
            a = min(a , counttext[i] // count[i])
        return a
        
