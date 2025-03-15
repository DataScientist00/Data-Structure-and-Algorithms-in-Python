#problem link-->> https://leetcode.com/problems/house-robber-iv/description/


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def canrob(mid):
            count , i = 0 , 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1
            return count >= k


        left , right = min(nums) , max(nums)
        answer = right
        while left <= right:
            mid = (left + right) // 2
            if canrob(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
        
