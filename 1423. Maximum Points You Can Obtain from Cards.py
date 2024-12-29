#problem link-->> https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l , r = 0 , len(cardPoints) - k
        res = 0
        total = sum(cardPoints[r:])
        res = total
        while r < len(cardPoints):
            total += (cardPoints[l] - cardPoints[r])
            res = max(total , res)
            l += 1
            r += 1
        return res
        
