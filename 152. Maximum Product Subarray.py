#problem link-->> https://leetcode.com/problems/maximum-product-subarray/description/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxn , minn = 1 , 1
        for n in nums:
            temp = maxn*n
            maxn = max(n*maxn , n*minn , n)
            minn = min(temp , n*minn , n)
            res = max(maxn,res)
        return res
        
