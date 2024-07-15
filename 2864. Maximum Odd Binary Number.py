#problem link-->> https://leetcode.com/problems/maximum-odd-binary-number/description/


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = [c for c in s]
        left = 0
        for i in range(len(s)):
            if s[i] == '1':
                s[left],s[i]=s[i],s[left]
                left += 1
        s[left-1],s[len(s)-1]=s[len(s)-1],s[left-1]
        return "".join(s)


        
