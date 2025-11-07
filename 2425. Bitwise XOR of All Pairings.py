# problem link-->> https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor = 0
        if len(nums1) % 2 == 1:
            for n in nums2:
                xor ^= n

        if len(nums2) % 2 == 1:
            for n in nums1:
                xor ^= n
        return xor
        
