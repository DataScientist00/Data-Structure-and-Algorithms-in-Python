# problem link-->> https://leetcode.com/problems/count-number-of-teams/description/


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        memo = {}
        def dp(i , ascend , count):
            if (i , ascend , count) in memo:
                return memo[(i , ascend , count)]
            if count == 3:
                return 1
            if len(rating) <= i:
                return 0
            res = 0
            for j in range(i+1 , len(rating)):
                if rating[i] < rating[j] and ascend:
                    res += dp(j , ascend , count + 1)
                if rating[i] > rating[j] and not ascend:
                    res += dp(j , ascend , count + 1)
            memo[(i , ascend , count)] = res
            return memo[(i , ascend , count)]
        res = 0
        for i in range(len(rating)):
            res += dp(i , True , 1)
            res += dp(i , False , 1)
        return res
        
