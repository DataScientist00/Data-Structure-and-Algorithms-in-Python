# problem link-->> https://leetcode.com/problems/best-sightseeing-pair/description/


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        prev_max = values[0]
        ans = float('-inf')
        for i in range(1,len(values)):
            prev_max -= 1
            ans = max(ans , prev_max + values[i])
            prev_max = max(prev_max , values[i])
        return ans


        
