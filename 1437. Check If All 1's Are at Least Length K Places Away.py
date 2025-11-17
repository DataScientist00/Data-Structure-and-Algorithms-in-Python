# problem link-->> https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one_idx = -1
        for i , n in enumerate(nums):
            if n == 1:
                if prev_one_idx == -1:
                    prev_one_idx = i
                    continue
                else:
                    if i - prev_one_idx <= k:
                        return False
                    prev_one_idx = i
        return True
        
