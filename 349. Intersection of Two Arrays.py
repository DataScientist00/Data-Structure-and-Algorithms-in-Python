#problem link-->>> https://leetcode.com/problems/intersection-of-two-arrays/description/


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2 , nums1
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.add(nums1[i])
        return ans
        
