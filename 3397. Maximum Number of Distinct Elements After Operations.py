# problem link-->> https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description/



class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = float('-inf')
        count = 0
        for n in nums:
            maxval = n - k
            if prev < maxval:
                prev = maxval
                count += 1
            elif prev < n+k:
                count += 1
                prev = prev + 1
        return count
