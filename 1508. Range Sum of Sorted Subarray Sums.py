# problem link-->> https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        M = 10 ** 9 + 7
        arr = []
        for window in range(1,len(nums)+1):
            l = 0
            total = 0
            for r in range(len(nums)):
                total += nums[r]
                if r-l+1 == window:
                    arr.append(total)
                    total -= nums[l]
                    l += 1
        arr.sort()
        return (sum(arr[left-1:right])) % M
        
