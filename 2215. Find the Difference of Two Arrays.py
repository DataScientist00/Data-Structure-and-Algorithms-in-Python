#problem link--->> https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numsset1,numsset2 = set(nums1) , set(nums2)
        res1,res2 = set(),set()
        for i in nums1:
            if i not in numsset2:
                res1.add(i)
        for i in nums2:
            if i not in numsset1:
                res2.add(i)
        return [res1 , res2]

        
