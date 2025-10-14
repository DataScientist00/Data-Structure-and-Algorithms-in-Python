# problem link-->> https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        l = 0
        res = 0
        total = 0
        for r in range(len(nums)):
            cnt[nums[r]] += 1
            total += nums[r]
            if r-l+1 > k:
                cnt[nums[l]] -= 1
                if cnt[nums[l]] == 0:
                    cnt.pop(nums[l])
                total -= nums[l]
                l += 1
            if r-l+1 == k and len(cnt) == k:
                res = max(res , total)
        return res

        
