# problem link--> https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        t = len(nums) // 2
        for k , v in cnt.items():
            if v == t:
                return k
        
