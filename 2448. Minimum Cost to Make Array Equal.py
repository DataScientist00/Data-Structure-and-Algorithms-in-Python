# problem link-->> https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def total_cost(mid):
            total=0
            for i in range(len(nums)):
                total += abs(nums[i]-mid) * cost[i]
            return total

        l = min(nums)
        r = max(nums)
        while l <= r:
            mid = (l+r)//2
            
            cost1 = total_cost(mid)
            cost2 = total_cost(mid+1)
            ans = min(cost1 , cost2)

            if cost2 > cost1:
                r = mid -1
            else:
                l = mid + 1
        return ans
