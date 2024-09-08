#problem link-->> https://leetcode.com/problems/minimum-cost-for-tickets/description/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dp(i ):
            if i == len(days):
                return 0
            if i in memo:
                return memo[i]
            j = i
            while j < len(days) and days[j] < days[i] + 1:
                j +=1
            a = dp(j) + costs[0]
            while j < len(days) and days[j] < days[i] +7:
                j +=1
            b = dp(j) + costs[1]
            while j < len(days) and days[j] < days[i] + 30:
                j +=1
            c = dp(j) + costs[2]
            memo[i] = min(a,b,c)
            return memo[i]
        return dp(0)


        
