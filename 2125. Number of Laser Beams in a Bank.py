
# problem link-->> https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = bank[0].count('1')
        ans = 0
        temp = 0
        for i in range(1 , len(bank)):
            temp = bank[i].count('1')
            if temp:
                ans += (res * temp)
                res = temp
        return ans
        
