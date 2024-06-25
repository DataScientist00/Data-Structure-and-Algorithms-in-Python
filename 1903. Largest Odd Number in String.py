#problem link--->>> https://leetcode.com/problems/largest-odd-number-in-string/description/


class Solution:
    def largestOddNumber(self, num: str) -> str:
        size = len(num)-1
        index=0
        while size >= 0:
            if int(num[size]) % 2 == 1:
                index = size
                return num[:index+1]
            size -= 1
        return ''


        
