# problem link-->> https://leetcode.com/problems/smallest-integer-divisible-by-k/description/


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        cnt = 1
        num = 1
        if k % 2 ==0 or k % 5 == 0:
            return -1
        while True:
            if num % k == 0:
                return cnt
            else:
                num = num * 10 + 1
                cnt += 1
        
