#problem link-->>> https://leetcode.com/problems/buy-two-chocolates

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = float("inf")

        for m in prices:
            if m < min1:
                min1,min2 = m,min1
            elif m < min2:
                min2 = m
        total = money - min1 - min2
        return total if total >= 0 else money
        
