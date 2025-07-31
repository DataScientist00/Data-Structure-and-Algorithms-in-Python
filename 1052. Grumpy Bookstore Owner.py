# problem link-->> https://leetcode.com/problems/grumpy-bookstore-owner/description/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        summ = 0
        for n in range(len(customers)):
            if not grumpy[n]:
                summ += customers[n]
        l = 0
        total , res = 0,0
        for r in range(len(customers)):
            total += customers[r] if grumpy[r] == 1 else 0
            if r >= minutes:
                total -= customers[l] if grumpy[l] ==1 else 0
                l += 1
            res = max(res , total)
        return summ + res
