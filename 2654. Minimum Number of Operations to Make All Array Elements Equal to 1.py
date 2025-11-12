# problem link-->> https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description/


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_one = 0
        for n in nums:
            if n == 1:
                count_one += 1

        if count_one > 0:
            return len(nums) - count_one

        ans = float('inf')
        
        for i in range(len(nums)):
            gcd = nums[i]
            for j in range(i+1 , len(nums)):
                gcd = math.gcd(gcd , nums[j])
                if gcd == 1:
                    ans = min(ans , j - i)
                    break

        return ans + len(nums) - 1 if ans != float('inf') else -1
