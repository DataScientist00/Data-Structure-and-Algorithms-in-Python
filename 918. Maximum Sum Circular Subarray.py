# problem link-->> http://leetcode.com/problems/maximum-sum-circular-subarray/description/


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax , globalmin = nums[0] , nums[0]
        minn , maxx = 0 , 0
        total = 0

        for n in nums:
            minn = min(minn + n , n)
            maxx = max(maxx + n , n)
            total += n

            globalmax = max(maxx , globalmax)
            globalmin = min(minn , globalmin)

        return max( globalmax , total - globalmin) if globalmax > 0 else globalmax

        
