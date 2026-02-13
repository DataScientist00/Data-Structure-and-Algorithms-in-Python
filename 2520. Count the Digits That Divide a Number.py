# problem link -- >> https://leetcode.com/problems/count-the-digits-that-divide-a-number


class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        ans = 0
        while temp != 0:
            digit = temp % 10
            if num % digit == 0:
                ans += 1
            temp = temp // 10
        return ans
        
