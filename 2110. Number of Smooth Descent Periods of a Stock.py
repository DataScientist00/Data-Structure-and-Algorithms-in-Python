# problem link-->> https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 1
        size = 1
        for r in range(1,len(prices)):
            if prices[r] + 1 == prices[r-1]:
                size += 1
            else:
                size = 1
            ans += size
        return ans
        
