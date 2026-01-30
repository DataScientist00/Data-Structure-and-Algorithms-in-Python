#   problem lnk -- >>> https://leetcode.com/problems/compute-alternating-sum/description/


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even = 0 
        odd = 0 
        for i,n in enumerate(nums):
            if i % 2 == 0:
                even += n
            else:
                odd += n
        return even - odd

        
