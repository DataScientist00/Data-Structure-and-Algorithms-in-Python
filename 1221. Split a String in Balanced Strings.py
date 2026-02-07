# problem link -- >> https://leetcode.com/problems/split-a-string-in-balanced-strings/description/


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        a=0
        it=0
        for i in s:
            if i=='R':
                a+=1
            elif i=='L':
                a-=1
            if a==0:
                it+=1
        return it
        
