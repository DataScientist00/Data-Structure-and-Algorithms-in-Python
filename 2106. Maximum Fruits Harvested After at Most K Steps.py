# problem link-->> https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/description/

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        maxres = 0
        total = 0
        l = 0
        for r in range(n):
            total += fruits[r][1]
            while l <= r:
                leftpos = fruits[l][0]
                rightpos = fruits[r][0]

                leftfirst = abs(startPos - leftpos) + (rightpos - leftpos)
                rgihtfirst = abs(startPos - rightpos) + (rightpos - leftpos)

                if min(leftfirst , rgihtfirst) <= k:
                    break

                total -= fruits[l][1]
                l += 1
            maxres = max(maxres , total)
        return maxres

        
