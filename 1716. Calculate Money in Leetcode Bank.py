#problem link--->>> https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/


class Solution:
    def totalMoney(self, n: int) -> int:
        deposit = 1
        day = 0
        res = 0

        while day < n:
            res += deposit
            deposit += 1
            day += 1

            if day % 7 == 0 :
                deposit = 1 + day // 7
        return res
        
